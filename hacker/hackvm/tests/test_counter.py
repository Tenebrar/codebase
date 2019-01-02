from pytest import mark, param, raises

from hacker.hackvm.counter import IterationCounter


@mark.parametrize('max', (
    param(0),
    param(1),
    param(100),
))
def test_increment(max: int) -> None:
    counter = IterationCounter(max)

    for _ in range(max):
        counter.increment()

    with raises(RuntimeError):
        counter.increment()


def test_negative_input() -> None:
    with raises(ValueError):
        IterationCounter(-1)
