from typing import Dict, NewType, Tuple

from charsheet.constants import Size

Damage = NewType('Damage', Tuple[int, int])

DICE_PROGRESSION_CHART: Dict[Damage, int] = {
    (1, 1): 1,
    (1, 2): 2,
    (1, 3): 3,
    (1, 4): 4,
    (1, 6): 5,
    (1, 8): 6,
    (1, 10): 7,
    (2, 6): 8,
    (2, 8): 9,
    (3, 6): 10,
    (3, 8): 11,
    (4, 6): 12,
    (4, 8): 13,
    (6, 6): 14,
    (6, 8): 15,
    (8, 6): 16,
    (8, 8): 17,
    (12, 6): 18,
    (12, 8): 19,
    (16, 6): 20
}
INVERSE_DICE_PROGRESSION_CHART: Dict[int, Damage] = {v: k for k, v in DICE_PROGRESSION_CHART.items()}

SMALL_OR_LOWER = [Size.FINE, Size.DIMINUTIVE, Size.TINY, Size.SMALL]
MEDIUM_OR_LOWER = [Size.FINE, Size.DIMINUTIVE, Size.TINY, Size.SMALL, Size.MEDIUM]


def change_size(increase: bool, damage: Damage, initial_size: Size) -> Damage:
    """
    Change the damage of a weapon up or down one size category

    :param increase: Whether the damage should be increased (True) or decreased (False)
    :param damage: The initial Damage (as a tuple(int, int), e.g. 2d6 -> (2, 6))
    :param initial_size: The effective Size of the initial damamge
    :return: The changed Damage (as a tuple(int, int), e.g. 2d6 -> (2, 6))
    :raises KeyError: When the rules for increase in size are ill-defined for the requested inputs
        This can happen at the extremes (e.g reducing 1d1) or with some amounts of certain die types (e.g. 5d4)
    :raises AssertionError: When invalid inputs are passed, e.g. 0d6 or 1d0 as Damage
    """
    assert damage[0] > 0 and damage[1] > 0

    # Handle multiple d10s
    if damage[0] >= 2 and damage[1] == 10:
        return (damage[0] * 2, 8) if increase else (damage[0], 8)

    # Handle multiple d4s (the rules are ill-defined for some amounts, e.g. 5d4)
    if damage[0] % 2 == 0 and damage[1] == 4:
        damage = (damage[0] / 2, 8)
    elif damage[0] % 3 == 0 and damage[1] == 4:
        damage = ((damage[0] / 3) * 2, 6)

    # Handle multiple d12s
    if damage[1] == 12:
        damage = (damage[0] * 2, 12)

    try:
        original_index = DICE_PROGRESSION_CHART[damage]
    except KeyError as e:
        if damage[1] == 6:
            pass
        elif damage[1] == 8:
            pass
        else:
            raise e

    if increase:
        index_change = 2
        if initial_size in SMALL_OR_LOWER or original_index <= DICE_PROGRESSION_CHART[(1, 6)]:
            index_change = 1
    else:
        index_change = -2
        if initial_size in MEDIUM_OR_LOWER or original_index <= DICE_PROGRESSION_CHART[(1, 8)]:
            index_change = -1

    return INVERSE_DICE_PROGRESSION_CHART[original_index + index_change]


print(change_size(False, (1, 1), Size.MEDIUM))

for i in range(10 - 1, 0, -1):
    print(i)
