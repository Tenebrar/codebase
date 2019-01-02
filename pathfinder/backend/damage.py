from enum import Enum, unique
from typing import List, Optional

from pathfinder.backend.dice import Dice


@unique
class DamageType(Enum):
    """
    The types of damage possible in the Pathfinder system.
    A distinction is made between weapon damage (susceptible to Damage Reduction) and energy damage (susceptible to
    energy resistance)
    """
    # Weapon damage
    BLUDGEONING = (False, 'Bludgeoning')
    PIERCING = (False, 'Piercing')
    SLASHING = (False, 'Slashing')
    # Energy damage
    ACID = (True, 'Acid')
    COLD = (True, 'Cold')
    ELECTRICITY = (True, 'Electricity')
    FIRE = (True, 'Fire')
    FORCE = (True, 'Force')
    SONIC = (True, 'Sonic')
    # Special energy damage
    POSITIVE = (True, 'Positive')
    NEGATIVE = (True, 'Negative')

    def __init__(self, energy: bool, label: str) -> None:
        """
        :param energy: Whether the damage type is energy damage (susceptible to energy resistance)
        :param label: A str to represent the damage type
        """
        self.energy = energy
        self.label = label

    def __str__(self) -> str:
        return self.label


class PartialDamage(object):
    """
    An object representing partial damage from which full damage is built.
    E.g. A dagger can deal its regular damage, sneak attack damage and fire damage because of the flaming property.
    These are 3 separate PartialDamage instances
    """
    def __init__(self, dice: Optional[Dice]=None, fixed=0, types: Optional[List[List[DamageType]]]=None,
                 lethal: bool=True, precision: bool=False, special_weapon_quality=False) -> None:
        """
        :param dice: The damage dice (default=None)
        :param fixed: The fixed damage (default=0)
        :param types: The DamageTypes (default=BLUDGEONING).
        This is given as a List of options, where each option is a List of DamageTypes.
        E.g. a dagger can deal piercing OR slashing damage, so it would have types:
        [[DamageType.PIERCING], [DamageType.SLASHING]]
        A morningstar deals bludgeoning AND piercing damage, so it would have types:
        [[DamageType.BLUDGEONING, DamageType.PIERCING]]
        :param lethal: whether the damage is lethal (default=True)
        :param precision: whether the damage is precision damage (default=False)
        :param special_weapon_quality: whether the damage originates from a special weapon quality, such as flaming
        (default=False)
        :raises ValueError: if no dice or fixed damage is given
        """
        if not dice and not fixed:
            raise ValueError('Cannot have damage without dice or fixed value')

        if not types:
            types = [[DamageType.BLUDGEONING]]
        # Because the List of Lists of DamageTypes is rather complex, I do extensive validation on it
        for t in types:
            if not t or not isinstance(t, List):
                raise ValueError(f"Disallowed damage type '{t}' in '{types}'")
            for t2 in t:
                if not isinstance(t2, DamageType):
                    raise ValueError(f"Disallowed damage type '{t2}' in '{types}'")

        self.dice: Optional[Dice] = dice
        self.fixed: int = fixed
        self.types: List[List[DamageType]] = types
        self.lethal = lethal
        self.precision = precision
        self.special_weapon_quality = special_weapon_quality

    def __str__(self) -> str:
        result = ''
        if self.dice:
            result += str(self.dice)
        if self.fixed:
            if self.dice:
                result += '+'
            result += str(self.fixed)
        # For now, only print a single energy type
        if len(self.types) == 1 and len(self.types[0]) == 1:
            t = self.types[0][0]
            if t.energy:
                result += f' {t}'
        else:
            result += ' Complex'
        if not self.lethal:
            result += ' nonlethal'
        if self.precision:
            result += ' precision'

        return result

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'


class Damage(object):
    """ An object representing the damage that may be done (e.g. by a weapon) """
    def __init__(self, partials: List[PartialDamage]) -> None:
        if not partials:
            raise ValueError(f"partials must be a non-empty List, not '{partials}'")

        self.partials = partials

    def __str__(self):
        return ' + '.join([str(partial) for partial in self.partials])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'
