from datetime import datetime
from decimal import Decimal
from typing import Any, Callable, Container, Iterable, Optional, Type, TypeVar, Union


# Single-args predicates
def is_strict_positive(i: Union[int, float, Decimal]) -> bool:
    return i > 0


def is_positive(i: Union[int, float, Decimal]) -> bool:
    return i >= 0


def is_strict_negative(i: Union[int, float, Decimal]) -> bool:
    return i < 0


def is_negative(i: Union[int, float, Decimal]) -> bool:
    return i <= 0


def is_even(i: int) -> bool:
    return i % 2 == 0


def is_odd(i: int) -> bool:
    return i % 2 == 1


def is_not_none(obj: Optional[object]) -> bool:
    return obj is not None


def is_in(allowed: Container[Any]) -> Callable[[Any], bool]:
    def _is_in(value: Any) -> bool:
        return value in allowed
    return _is_in


def is_not_in(disallowed: Container[Any]) -> Callable[[Any], bool]:
    def _is_not_in(value: Any) -> bool:
        return value not in disallowed
    return _is_not_in


def is_type(tipe: Type) -> Callable[[Any], bool]:
    def _is_type(value: Any) -> bool:
        return isinstance(value, tipe)
    return _is_type


def at_least(minimum: int) -> Callable[[int], bool]:
    def _at_least(i: int):
        return i >= minimum
    _at_least.__name__ = f'_at_least_{minimum}'
    return _at_least


X = TypeVar('X')


def each(predicate: Callable[[X], bool]) -> Callable[[Iterable[X]], bool]:
    def _each(l: Iterable[X]) -> bool:
        return all(predicate(i) for i in l)
    _each.__name__ = f'_each_{predicate.__name__}'
    return _each



# No-args predicates
def after(time: datetime, now: Callable[[], datetime]=datetime.now) -> Callable[[], bool]:
    def _after() -> bool:
        return now() > time
    return _after


def before(time: datetime, now: Callable[[], datetime]=datetime.now) -> Callable[[], bool]:
    def _before() -> bool:
        return now() < time
    return _before


def not_implemented_yet() -> bool:
    return False


# Multi-args predicates
def is_greater_than(a, b) -> bool:
    return a > b


def is_greater_than_or_equal(a, b) -> bool:
    return a >= b


def is_less_than(a, b) -> bool:
    return a < b


def is_less_than_or_equal(a, b) -> bool:
    return a <= b


def is_different(a, b) -> bool:
    return a != b
