from pytest import mark, param
from typing import NoReturn

from sandbox.pathfinder.ability_scores import get_single_point_buy_cost
from sandbox.pathfinder.types import AbilityScore


@mark.parametrize('ability_score, cost', (
    param(0, None),
    param(1, None),
    param(2, None),
    param(3, None),
    param(4, None),
    param(5, None),
    param(6, None),
    param(7, -4),
    param(8, -2),
    param(9, -1),
    param(10, 0),
    param(11, 1),
    param(12, 2),
    param(13, 3),
    param(14, 5),
    param(15, 7),
    param(16, 10),
    param(17, 13),
    param(18, 17),
    param(19, None),
    param(20, None),
    param(21, None),
    param(22, None),
))
def test_get_single_point_buy_cost(ability_score: AbilityScore, cost: int) -> NoReturn:
    assert get_single_point_buy_cost(ability_score) == cost
