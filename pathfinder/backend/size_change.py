from typing import Dict

from pathfinder.backend.dice import Dice, DieType
from pathfinder.charsheet.constants import Size


DICE_PROGRESSION_CHART: Dict[Dice, int] = {
    Dice(1, DieType.D1): 1,
    Dice(1, DieType.D2): 2,
    Dice(1, DieType.D3): 3,
    Dice(1, DieType.D4): 4,
    Dice(1, DieType.D6): 5,
    Dice(1, DieType.D8): 6,
    Dice(1, DieType.D10): 7,
    Dice(2, DieType.D6): 8,
    Dice(2, DieType.D8): 9,
    Dice(3, DieType.D6): 10,
    Dice(3, DieType.D8): 11,
    Dice(4, DieType.D6): 12,
    Dice(4, DieType.D8): 13,
    Dice(6, DieType.D6): 14,
    Dice(6, DieType.D8): 15,
    Dice(8, DieType.D6): 16,
    Dice(8, DieType.D8): 17,
    Dice(12, DieType.D6): 18,
    Dice(12, DieType.D8): 19,
    Dice(16, DieType.D6): 20
}
INVERSE_DICE_PROGRESSION_CHART: Dict[int, Dice] = {v: k for k, v in DICE_PROGRESSION_CHART.items()}


def change_size(increase: bool, damage: Dice, initial_size: Size) -> Dice:
    """
    Change the damage of a weapon up or down one size category

    :param increase: Whether the size should be increased (True) or decreased (False)
    :param damage: The initial damage Dice
    :param initial_size: The effective Size of the initial damamge
    :return: The changed damage Dice
    :raises KeyError: When the rules for increase in size are ill-defined for the requested inputs
        This can happen at the extremes (e.g reducing 1d1) or with some amounts of certain die types (e.g. 5d4)
    """
    # Handle multiple d10s
    if damage.dice >= 2 and damage.die_type == 10:
        return Dice(damage.dice * 2 if increase else damage.dice, DieType.D8)

    # Handle multiple d4s (the rules are ill-defined for some amounts, e.g. 5d4)
    if damage.dice % 2 == 0 and damage.die_type == 4:
        damage = Dice(damage.dice / 2, DieType.D8)
    elif damage.dice % 3 == 0 and damage.die_type == 4:
        damage = Dice((damage.dice / 3) * 2, DieType.D6)

    # Handle d12s
    if damage.die_type == 12:
        damage = Dice(damage.dice * 2, DieType.D6)

    original_index = 0
    try:
        original_index = DICE_PROGRESSION_CHART[damage]
    except KeyError as e:
        if damage.die_type == 6:
            pass  # TODO
        elif damage.die_type == 8:
            pass  # TODO
        else:
            raise e

    if increase:
        index_change = 2
        if initial_size <= Size.SMALL or original_index <= DICE_PROGRESSION_CHART[Dice(1, DieType.D6)]:
            index_change = 1
    else:
        index_change = -2
        if initial_size >= Size.MEDIUM or original_index <= DICE_PROGRESSION_CHART[Dice(1, DieType.D8)]:
            index_change = -1

    return INVERSE_DICE_PROGRESSION_CHART[original_index + index_change]
