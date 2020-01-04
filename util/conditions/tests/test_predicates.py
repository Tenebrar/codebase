from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any, Callable, Container, Iterable, Type

from pytest import mark, param

from util.conditions.predicates import (
    each, is_after, is_before, is_even, is_greater_than, is_greater_than_multi, is_greater_than_or_equal,
    is_greater_than_or_equal_multi, is_in, is_less_than, is_less_than_multi, is_less_than_or_equal,
    is_less_than_or_equal_multi, is_negative, is_not_implemented_yet, is_not_in, is_not_none, is_odd, is_positive,
    is_strict_negative, is_strict_positive, is_type
)


@mark.parametrize('value, expected', (
    param(1, True),
    param(0.1, True),
    param(Decimal('0.1'), True),
    param(0, False),
    param(Decimal('-0.1'), False),
    param(-0.1, False),
    param(-1, False),
))
def test_is_strict_positive(value: Any, expected: bool) -> None:
    assert is_strict_positive(value) == expected


@mark.parametrize('value, expected', (
    param(1, True),
    param(0.1, True),
    param(Decimal('0.1'), True),
    param(0, True),
    param(Decimal('-0.1'), False),
    param(-0.1, False),
    param(-1, False),
))
def test_is_positive(value: Any, expected: bool) -> None:
    assert is_positive(value) == expected


@mark.parametrize('value, expected', (
    param(1, False),
    param(0.1, False),
    param(Decimal('0.1'), False),
    param(0, False),
    param(Decimal('-0.1'), True),
    param(-0.1, True),
    param(-1, True),
))
def test_is_strict_negative(value: Any, expected: bool) -> None:
    assert is_strict_negative(value) == expected


@mark.parametrize('value, expected', (
    param(1, False),
    param(0.1, False),
    param(Decimal('0.1'), False),
    param(0, True),
    param(Decimal('-0.1'), True),
    param(-0.1, True),
    param(-1, True),
))
def test_is_negative(value: Any, expected: bool) -> None:
    assert is_negative(value) == expected


@mark.parametrize('value, expected', (
    param(1000000, True),
    param(1000001, False),
    param(3, False),
    param(2, True),
    param(1, False),
    param(0, True),
    param(-1, False),
    param(-2, True),
    param(-3, False),
))
def test_is_even(value: Any, expected: bool) -> None:
    assert is_even(value) == expected


@mark.parametrize('value, expected', (
    param(1000000, False),
    param(1000001, True),
    param(3, True),
    param(2, False),
    param(1, True),
    param(0, False),
    param(-1, True),
    param(-2, False),
    param(-3, True),
))
def test_is_odd(value: Any, expected: bool) -> None:
    assert is_odd(value) == expected


@mark.parametrize('value, expected', (
    param(None, False),
    param(object(), True),
    param(0, True),
    param('', True),
    param([], True),
    param({}, True),
))
def test_is_not_none(value: Any, expected: bool) -> None:
    assert is_not_none(value) == expected


@mark.parametrize('value, container, expected', (
    param('a', ['a', 'b', 'c'], True),
    param('a', ['b', 'c'], False),
    param('a', [], False),
    param(None, [], False),
    param(None, [None], True),
))
def test_is_in(value: Any, container: Container[Any], expected: bool) -> None:
    predicate = is_in(container)
    assert predicate(value) == expected


@mark.parametrize('value, container, expected', (
    param('a', ['a', 'b', 'c'], False),
    param('a', ['b', 'c'], True),
    param('a', [], True),
    param(None, [], True),
    param(None, [None], False),
))
def test_is_not_in(value: Any, container: Container[Any], expected: bool) -> None:
    predicate = is_not_in(container)
    assert predicate(value) == expected


@mark.parametrize('value, tipe, expected', (
    param('a', str, True),
    param('a', object, True),
    param(None, type(None), True),
    param('a', int, False),
    param(None, str, False),
))
def test_is_type(value: Any, tipe: Type, expected: bool) -> None:
    predicate = is_type(tipe)
    assert predicate(value) == expected


@mark.parametrize('value, minimum, expected', (
    param(4, 3, True),
    param(4, 3.9, True),
    param(4, 4, False),
    param(4, 5, False),
))
def test_is_greater_than(value: Any, minimum: Any, expected: bool) -> None:
    predicate = is_greater_than(minimum)
    assert predicate(value) == expected


@mark.parametrize('value, minimum, expected', (
    param(4, 3, True),
    param(4, 3.9, True),
    param(4, 4, True),
    param(4, 5, False),
))
def test_is_greater_than_or_equal(value: Any, minimum: Any, expected: bool) -> None:
    predicate = is_greater_than_or_equal(minimum)
    assert predicate(value) == expected


@mark.parametrize('value, maximum, expected', (
    param(4, 3, False),
    param(4, 3.9, False),
    param(4, 4, False),
    param(4, 5, True),
))
def test_is_less_than(value: Any, maximum: Any, expected: bool) -> None:
    predicate = is_less_than(maximum)
    assert predicate(value) == expected


@mark.parametrize('value, maximum, expected', (
    param(4, 3, False),
    param(4, 3.9, False),
    param(4, 4, True),
    param(4, 5, True),
))
def test_is_less_than_or_equal(value: Any, maximum: Any, expected: bool) -> None:
    predicate = is_less_than_or_equal(maximum)
    assert predicate(value) == expected


@mark.parametrize('predicate, container, expected', (
    param(is_positive, [1, 2], True),
    param(is_positive, [1, -2], False),
))
def test_each(predicate: Callable[[Any], bool], container: Iterable[Any], expected: bool) -> None:
    _predicate = each(predicate)
    assert _predicate(container) == expected


@mark.parametrize('time, now, expected', (
    param(datetime.now() - timedelta(days=1), datetime.now, True),
    param(datetime.now() + timedelta(days=1), datetime.now, False),
    param(datetime(2035, 5, 7), lambda: datetime(2090, 9, 4), True),
    param(datetime(2035, 5, 7), lambda: datetime(2020, 9, 4), False),
))
def test_is_after(time: datetime, now: Callable[[], datetime], expected: bool) -> None:
    predicate = is_after(time, now)
    assert predicate() == expected


@mark.parametrize('time, now, expected', (
    param(datetime.now() - timedelta(days=1), datetime.now, False),
    param(datetime.now() + timedelta(days=1), datetime.now, True),
    param(datetime(2035, 5, 7), lambda: datetime(2090, 9, 4), False),
    param(datetime(2035, 5, 7), lambda: datetime(2020, 9, 4), True),
))
def test_is_before(time: datetime, now: Callable[[], datetime], expected: bool) -> None:
    predicate = is_before(time, now)
    assert predicate() == expected


def test_in_not_implemented_yet() -> None:
    assert is_not_implemented_yet() == False


@mark.parametrize('a, b, expected', (
    param(4, 3, True),
    param(4, 3.9, True),
    param(4, 4, False),
    param(4, 5, False),
))
def test_is_greater_than_multi(a: Any, b: Any, expected: bool) -> None:
    assert is_greater_than_multi(a, b) == expected


@mark.parametrize('a, b, expected', (
    param(4, 3, True),
    param(4, 3.9, True),
    param(4, 4, True),
    param(4, 5, False),
))
def test_is_greater_than_or_equal_multi(a: Any, b: Any, expected: bool) -> None:
    assert is_greater_than_or_equal_multi(a, b) == expected


@mark.parametrize('a, b, expected', (
    param(4, 3, False),
    param(4, 3.9, False),
    param(4, 4, False),
    param(4, 5, True),
))
def test_is_less_than_multi(a: Any, b: Any, expected: bool) -> None:
    assert is_less_than_multi(a, b) == expected


@mark.parametrize('a, b, expected', (
    param(4, 3, False),
    param(4, 3.9, False),
    param(4, 4, True),
    param(4, 5, True),
))
def test_is_less_than_or_equal_multi(a: Any, b: Any, expected: bool) -> None:
    assert is_less_than_or_equal_multi(a, b) == expected
