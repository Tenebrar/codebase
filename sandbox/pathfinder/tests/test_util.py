from pytest import mark, param
from typing import NoReturn, Tuple

from sandbox.pathfinder.util import scalar_multiply


@mark.parametrize('values, scalar, expected', (
    param((1.2, 3.4, 5.0), 1.0, (1.2, 3.4, 5.0), id='identity'),
    param((1.2, 3.4, 5.0), 2.0, (2.4, 6.8, 10.0), id='simple multiplication'),
    param((1.2, 3.4, 5.0), 3.0, (1.2 * 3.0, 3.4 * 3.0, 5.0 * 3.0), id='expected rounding errors'),
    param((1.2, 3.4, 5.0, -9.2), 0.0, (0.0, 0.0, 0.0, 0.0), id='multiplication with 0'),
    param((1.2, 3.4, 5.0), -2.0, (-2.4, -6.8, -10.0), id='negative scalar'),
    param((-1.2, -3.4, -5.0), 2.0, (-2.4, -6.8, -10.0), id='negative values'),
    param((), 123.456, (), id='empty tuple'),
))
def test_scalar_multiply(values: Tuple[float, ...], scalar: float, expected: Tuple[float, ...]) -> NoReturn:
    result = scalar_multiply(values, scalar)

    assert result == expected
