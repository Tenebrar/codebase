from datetime import datetime
from decimal import Decimal
from typing import Any, Callable, Container, Optional, Type, Union


# Single-args predicates
def is_strict_positive(i: Union[int, float, Decimal]) -> bool:
    return i > 0


def is_positive(i: Union[int, float, Decimal]) -> bool:
    return i >= 0


def is_strict_negative(i: Union[int, float, Decimal]) -> bool:
    return i < 0


def is_negative(i: Union[int, float, Decimal]) -> bool:
    return i <= 0


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
