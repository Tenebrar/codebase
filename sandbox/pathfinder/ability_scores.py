from enum import Enum
from typing import Dict, Tuple, Optional

from sandbox.pathfinder.sizes import Size
from sandbox.pathfinder.types import AbilityScore, AbilityModifier, DistanceFeet, WeightLbs
from sandbox.pathfinder.util import scalar_multiply

# The defined costs for point buy calculation
ABILITY_SCORE_COSTS: Dict[AbilityScore, int] = {
    7: -4,
    8: -2,
    9: -1,
    10: 0,
    11: 1,
    12: 2,
    13: 3,
    14: 5,
    15: 7,
    16: 10,
    17: 13,
    18: 17,
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
    0: (0, 0, 0),  # This line was not present in the official table
    1: (3, 6, 10),
    2: (6, 13, 20),
    3: (10, 20, 30),
    4: (13, 26, 40),
    5: (16, 33, 50),
    6: (20, 40, 60),
    7: (23, 46, 70),
    8: (26, 53, 80),
    9: (30, 60, 90),
    10: (33, 66, 100),
    11: (38, 76, 115),
    12: (43, 86, 130),
    13: (50, 100, 150),
    14: (58, 116, 175),
    15: (66, 133, 200),
    16: (76, 153, 230),
    17: (86, 173, 260),
    18: (100, 200, 300),
    19: (116, 233, 350),
    20: (133, 266, 400),
    21: (153, 306, 460),
    22: (173, 346, 520),
    23: (200, 400, 600),
    24: (233, 466, 700),
    25: (266, 533, 800),
    26: (306, 613, 920),
    27: (346, 693, 1040),
    28: (400, 800, 1200),
    29: (466, 933, 1400),
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

    speed = speed - (speed % 5)  # round down to nearest multiple of 5 (effective speed)

    # Two thirds speed rounded up to nearest multiple of 5 feet
    reduced_speed = (speed * 2 // 3 + 4) // 5 * 5

    return DistanceFeet(reduced_speed)


# Definitions of the effects of three types of Load
class Load(Enum):
    # Max Dex, Armor check penalty, reduced speed, run multiplier
    LIGHT = (None, 0, False, 4)
    MEDIUM = (3, -3, True, 4)
    HEAVY = (1, -6, True, 3)
