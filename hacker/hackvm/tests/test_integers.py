from pytest import mark, param, raises

from hacker.hackvm.integers import MIN_INT, MAX_INT, verify_integer


@mark.parametrize('value', (
    param(-(1 << 63)),
    param(-100),
    param(-1),
    param(0),
    param(1),
    param(100),
    param((1 << 63) - 1),
))
def test_verify_integer(value: int) -> None:
    verify_integer(value)


@mark.parametrize('value', (
    param(-(1 << 63) - 1),
    param((1 << 63)),
))
def test_non_verifiable_integer(value: int) -> None:
    with raises(ValueError):
        verify_integer(value)
