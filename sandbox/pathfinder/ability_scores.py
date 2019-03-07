from enum import Enum
from typing import Dict, Tuple, Optional

from sandbox.pathfinder.sizes import Size
from sandbox.pathfinder.types import AbilityScore, AbilityModifier, DistanceFeet, WeightLbs
from sandbox.pathfinder.util import scalar_multiply

# The defined costs for point buy calculation
ABILITY_SCORE_COSTS: Dict[AbilityScore, int] = {
    AbilityScore(7): -4,
    AbilityScore(8): -2,
    AbilityScore(9): -1,
    AbilityScore(10): 0,
    AbilityScore(11): 1,
    AbilityScore(12): 2,
    AbilityScore(13): 3,
    AbilityScore(14): 5,
    AbilityScore(15): 7,
    AbilityScore(16): 10,
    AbilityScore(17): 13,
    AbilityScore(18): 17,
}

# The defined campaign types and their corresponding allotment of points for point buy
CAMPAIGN_TYPES: Dict[str, int] = {
    'Low Fantasy': 10,
    'Standard Fantasy': 15,
    'High Fantasy': 20,
    'Epic Fantasy': 25,
}


def get_single_point_buy_cost(base_ability_score: AbilityScore) -> Optional[int]:
    """
    :param base_ability_score: an ability score value
    :return: The point buy value for that ability score or None if undefined
    """
    try:
        return ABILITY_SCORE_COSTS[base_ability_score]
    except KeyError:
        return None


def get_point_buy_cost(base_strength: AbilityScore, base_constitution: AbilityScore, base_dexterity: AbilityScore,
                       base_intelligence: AbilityScore, base_wisdom: AbilityScore, base_charisma: AbilityScore)\
        -> Optional[int]:
    """
    :return: The sum of the point buy costs for all these ability scores of None if any is undefined
    """
    try:
        return sum(ABILITY_SCORE_COSTS[base_ability_score] for base_ability_score in
                   [base_strength, base_constitution, base_dexterity, base_intelligence, base_wisdom, base_charisma])
    except KeyError:
        return None


def get_modifier(ability_score: AbilityScore) -> AbilityModifier:
    """
    :param ability_score: An ability score
    :return: The modifier for that score
    """
    if ability_score < 0:
        raise ValueError(f'Ability score must be positive: {ability_score}')

    return AbilityModifier((ability_score - 10) // 2)


def get_bonus_spells(casting_ability_modifier: AbilityModifier) \
        -> Tuple[int, int, int, int, int, int, int, int, int, int]:
    """
    Get the amount of bonus spells of all spell levels for a given casting ability modifier

    Example usage: get_bonus_spells(AbilityModifier(3))[2] returns the amount of 2nd lvl bonus spells for a caster
    whose casting ability modifier is 3

    :param casting_ability_modifier: The ability modifier used for casting
    :return: a tuple containing the amount of bonus spells for each spell level
    """
    if casting_ability_modifier < -5:
        raise ValueError(f'Ability score modifier must be at least -5: {casting_ability_modifier}')

    return 0, \
        max(0, (casting_ability_modifier + 3) // 4), \
        max(0, (casting_ability_modifier + 2) // 4), \
        max(0, (casting_ability_modifier + 1) // 4), \
        max(0, (casting_ability_modifier + 0) // 4), \
        max(0, (casting_ability_modifier - 1) // 4), \
        max(0, (casting_ability_modifier - 2) // 4), \
        max(0, (casting_ability_modifier - 3) // 4), \
        max(0, (casting_ability_modifier - 4) // 4), \
        max(0, (casting_ability_modifier - 5) // 4)


CARRYING_CAPACITY: Dict[AbilityScore, Tuple[WeightLbs, WeightLbs, WeightLbs]] = {
    # Maximum weights for light, medium, heavy load
    AbilityScore(0): (WeightLbs(0), WeightLbs(0), WeightLbs(0)),  # This line was not present in the official table
    AbilityScore(1): (WeightLbs(3), WeightLbs(6), WeightLbs(10)),
    AbilityScore(2): (WeightLbs(6), WeightLbs(13), WeightLbs(20)),
    AbilityScore(3): (WeightLbs(10), WeightLbs(20), WeightLbs(30)),
    AbilityScore(4): (WeightLbs(13), WeightLbs(26), WeightLbs(40)),
    AbilityScore(5): (WeightLbs(16), WeightLbs(33), WeightLbs(50)),
    AbilityScore(6): (WeightLbs(20), WeightLbs(40), WeightLbs(60)),
    AbilityScore(7): (WeightLbs(23), WeightLbs(46), WeightLbs(70)),
    AbilityScore(8): (WeightLbs(26), WeightLbs(53), WeightLbs(80)),
    AbilityScore(9): (WeightLbs(30), WeightLbs(60), WeightLbs(90)),
    AbilityScore(10): (WeightLbs(33), WeightLbs(66), WeightLbs(100)),
    AbilityScore(11): (WeightLbs(38), WeightLbs(76), WeightLbs(115)),
    AbilityScore(12): (WeightLbs(43), WeightLbs(86), WeightLbs(130)),
    AbilityScore(13): (WeightLbs(50), WeightLbs(100), WeightLbs(150)),
    AbilityScore(14): (WeightLbs(58), WeightLbs(116), WeightLbs(175)),
    AbilityScore(15): (WeightLbs(66), WeightLbs(133), WeightLbs(200)),
    AbilityScore(16): (WeightLbs(76), WeightLbs(153), WeightLbs(230)),
    AbilityScore(17): (WeightLbs(86), WeightLbs(173), WeightLbs(260)),
    AbilityScore(18): (WeightLbs(100), WeightLbs(200), WeightLbs(300)),
    AbilityScore(19): (WeightLbs(116), WeightLbs(233), WeightLbs(350)),
    AbilityScore(20): (WeightLbs(133), WeightLbs(266), WeightLbs(400)),
    AbilityScore(21): (WeightLbs(153), WeightLbs(306), WeightLbs(460)),
    AbilityScore(22): (WeightLbs(173), WeightLbs(346), WeightLbs(520)),
    AbilityScore(23): (WeightLbs(200), WeightLbs(400), WeightLbs(600)),
    AbilityScore(24): (WeightLbs(233), WeightLbs(466), WeightLbs(700)),
    AbilityScore(25): (WeightLbs(266), WeightLbs(533), WeightLbs(800)),
    AbilityScore(26): (WeightLbs(306), WeightLbs(613), WeightLbs(920)),
    AbilityScore(27): (WeightLbs(346), WeightLbs(693), WeightLbs(1040)),
    AbilityScore(28): (WeightLbs(400), WeightLbs(800), WeightLbs(1200)),
    AbilityScore(29): (WeightLbs(466), WeightLbs(933), WeightLbs(1400)),
}


# Enum indicating the bipedal or quadrupedal state of a pathfinder character
class Pedalism(Enum):
    BIPED = 2
    QUADRUPED = 4


# Multipliers for carrying capacity based on Pedalism and Size
CARRYING_CAPACITY_MODIFIERS: Dict[Pedalism, Dict[Size, float]] = {
    Pedalism.BIPED: {
        Size.FINE: 1/8,
        Size.DIMINUTIVE: 1/4,
        Size.TINY: 1/2,
        Size.SMALL: 3/4,
        Size.MEDIUM: 1,
        Size.LARGE: 2,
        Size.HUGE: 4,
        Size.GARGANTUAN: 8,
        Size.COLOSSAL: 16,
    },
    Pedalism.QUADRUPED: {
        Size.FINE: 1/4,
        Size.DIMINUTIVE: 1/2,
        Size.TINY: 3/4,
        Size.SMALL: 1,
        Size.MEDIUM: 3/2,
        Size.LARGE: 3,
        Size.HUGE: 6,
        Size.GARGANTUAN: 12,
        Size.COLOSSAL: 24,
    },
}


def get_carrying_capacity(strength_score: AbilityScore, size: Size=Size.MEDIUM, pedalism: Pedalism=Pedalism.BIPED)\
        -> Tuple[WeightLbs, WeightLbs, WeightLbs]:
    """
    Get the different carrying capacities for a pathfinder character

    :param strength_score: The strength score of the character
    :param size: The Size of the character
    :param pedalism: The Pedalism of the character
    :return: a tuple holding the max weights for light, medium and heavy load
    """
    if strength_score < 0:
        raise ValueError(f'Strength score must be positive: {strength_score}')

    # Get value for medium biped
    if strength_score <= 29:
        capacity = CARRYING_CAPACITY[strength_score]
    else:
        base_index = AbilityScore(20 + (strength_score % 10))
        diff = (strength_score - base_index) // 10
        capacity = scalar_multiply(CARRYING_CAPACITY[base_index], 4**diff)

    # Modify value for pedalism and size
    capacity = scalar_multiply(capacity, CARRYING_CAPACITY_MODIFIERS[pedalism][size])

    return capacity


def get_overhead_lift_weight(strength_score: AbilityScore, size: Size=Size.MEDIUM, pedalism: Pedalism=Pedalism.BIPED)\
        -> WeightLbs:
    """
    Returns the overhead lift capacity of a pathfinder character
    """
    return get_carrying_capacity(strength_score, size, pedalism)[2]


def get_lift_weight(strength_score: AbilityScore, size: Size=Size.MEDIUM, pedalism: Pedalism=Pedalism.BIPED)\
        -> WeightLbs:
    """
    Returns the lift off ground capacity of a pathfinder character
    While doing this, a character loses dex bonus, moves max 5ft (as full-round action)
    """
    return WeightLbs(get_carrying_capacity(strength_score, size, pedalism)[2] * 2)


# Conditions affecting the effectiveness of pushing or dragging
class Conditions(Enum):
    FAVORABLE = 2
    NORMAL = 1
    UNFAVORABLE = 1/2


def get_push_or_drag_weight(strength_score: AbilityScore, size: Size=Size.MEDIUM, pedalism: Pedalism=Pedalism.BIPED,
                            conditions: Conditions=Conditions.NORMAL) -> WeightLbs:
    """
    Returns the push or drag capacity of a pathfinder character
    """
    return get_carrying_capacity(strength_score, size, pedalism)[2] * 5 * conditions.value


def get_reduced_speed(speed: DistanceFeet) -> DistanceFeet:
    """
    :param speed: a character's original speed
    :return: The new speed when reduced by either weight or armor
    """
    if speed < 0:
        raise ValueError(f'Speed must be positive: {speed}')

    speed = DistanceFeet(speed - (speed % 5))  # round down to nearest multiple of 5 (effective speed)

    # Two thirds speed rounded up to nearest multiple of 5 feet
    reduced_speed = (speed * 2 // 3 + 4) // 5 * 5

    return DistanceFeet(reduced_speed)


# Definitions of the effects of three types of Load
class Load(Enum):
    # Max Dex, Armor check penalty, reduced speed, run multiplier
    LIGHT = (None, 0, False, 4)
    MEDIUM = (3, -3, True, 4)
    HEAVY = (1, -6, True, 3)
