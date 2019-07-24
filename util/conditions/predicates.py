from datetime import datetime
from decimal import Decimal
from typing import Any, Callable, Container, Iterable, Optional, Type, TypeVar, Union

# We define predicates as functions that return a boolean: Callable[[Any,...], bool].
# This file contains (functions that return) predicates intended for use with the pre/post-condition system.
# We differentiate between predicates that take 0, 1 or more arguments.


# Single-args predicates
def is_strict_positive(i: Union[int, float, Decimal]) -> bool:
    """
    :param i: A number
    :return: Whether that number is greater than 0
    """
    return i > 0


def is_positive(i: Union[int, float, Decimal]) -> bool:
    """
    :param i: A number
    :return: Whether that number is greater than or equal to 0
    """
    return i >= 0


def is_strict_negative(i: Union[int, float, Decimal]) -> bool:
    """
    :param i: A number
    :return: Whether that number is less than 0
    """
    return i < 0


def is_negative(i: Union[int, float, Decimal]) -> bool:
    """
    :param i: A number
    :return: Whether that number is less than or equal to 0
    """
    return i <= 0


def is_even(i: int) -> bool:
    """
    :param i: An integer
    :return: Whether that number is even
    """
    return i % 2 == 0


def is_odd(i: int) -> bool:
    """
    :param i: An integer
    :return: Whether that number is odd
    """
    return i % 2 == 1


def is_not_none(obj: Optional[object]) -> bool:
    """
    :param obj: An object
    :return: True if the object is not None, False otherwise
    """
    return obj is not None


def is_in(allowed: Container[Any]) -> Callable[[Any], bool]:
    """
    :param allowed: A Container of allowed values
    :return: A predicate that checks if a value is within the allowed values
    """
    def predicate(value: Any) -> bool:
        """
        :param value: An object
        :return: Whether the object is within the allowed values
        """
        return value in allowed
    predicate.__name__ = f'_{is_in.__name__}_{allowed}'
    return predicate


def is_not_in(disallowed: Container[Any]) -> Callable[[Any], bool]:
    """
    :param disallowed: A Container of disallowed values
    :return: A predicate that checks if a value is not within the disallowed values
    """
    def predicate(value: Any) -> bool:
        """
        :param value: An object
        :return: Whether the object is not within the disallowed values
        """
        return value not in disallowed
    predicate.__name__ = f'_{is_not_in.__name__}_{disallowed}'
    return predicate


def is_type(tipe: Type) -> Callable[[Any], bool]:
    """
    :param tipe: A Type
    :return: A predicate that checks if an object is an instance of that Type
    """
    def predicate(value: Any) -> bool:
        """
        :param value: An object
        :return: Whether the object is an instance of the exprected Type
        """
        return isinstance(value, tipe)
    predicate.__name__ = f'_{is_type.__name__}_{tipe}'
    return predicate


def is_greater_than(minimum: Union[int, float, Decimal]) -> Callable[[Union[int, float, Decimal]], bool]:
    """
    :param minimum: A number
    :return: A predicate that checks if a value is more than the given number
    """
    def predicate(i: Union[int, float, Decimal]):
        """
        :param i: A number
        :return: Whether the number is more than the minimum
        """
        return i > minimum
    predicate.__name__ = f'_{is_greater_than.__name__}_{minimum}'
    return predicate


def is_greater_than_or_equal(minimum: Union[int, float, Decimal]) -> Callable[[Union[int, float, Decimal]], bool]:
    """
    :param minimum: A number
    :return: A predicate that checks if a value is at least the given number
    """
    def predicate(i: Union[int, float, Decimal]):
        """
        :param i: A number
        :return: Whether the number is at least the minimum
        """
        return i >= minimum
    predicate.__name__ = f'_{is_greater_than_or_equal.__name__}_{minimum}'
    return predicate


def is_less_than(maximum: Union[int, float, Decimal]) -> Callable[[Union[int, float, Decimal]], bool]:
    """
    :param maximum: A number
    :return: A predicate that checks if a value is less than the given number
    """
    def predicate(i: Union[int, float, Decimal]):
        """
        :param i: A number
        :return: Whether the number is less than the maximum
        """
        return i < maximum
    predicate.__name__ = f'_{is_less_than.__name__}_{maximum}'
    return predicate


def is_less_than_or_equal(maximum: Union[int, float, Decimal]) -> Callable[[Union[int, float, Decimal]], bool]:
    """
    :param maximum: A number
    :return: A predicate that checks if a value is at most the given number
    """
    def predicate(i: Union[int, float, Decimal]):
        """
        :param i: A number
        :return: Whether the number is at most the maximum
        """
        return i <= maximum
    predicate.__name__ = f'_{is_less_than_or_equal.__name__}_{maximum}'
    return predicate


X = TypeVar('X')


def each(predicate: Callable[[X], bool]) -> Callable[[Iterable[X]], bool]:
    """
    Special predicate factory used for checking all elements of container with the same predicate.

    :param predicate: A predicate that checks a single element
    :return: A predicate that checks each element of an Iterable
    """
    def _predicate(l: Iterable[X]) -> bool:
        """
        :param l: An iterable
        :return: Whether each element in the Iterable passes the predicate
        """
        return all(predicate(i) for i in l)
    _predicate.__name__ = f'_{each.__name__}_{predicate.__name__}'
    return _predicate


# No-args predicates
def is_after(time: datetime, now: Callable[[], datetime]=datetime.now) -> Callable[[], bool]:
    """
    :param time: A time
    :param now: A function to use to get the current time (defaults to datetime.now)
    :return: A predicate that checks if the current time is past the given time
    """
    def predicate() -> bool:
        """
        :return: Whether the current time is past the given time
        """
        return now() > time
    predicate.__name__ = f'_{is_after.__name__}_{datetime}'
    return predicate


def is_before(time: datetime, now: Callable[[], datetime]=datetime.now) -> Callable[[], bool]:
    """
    :param time: A time
    :param now: A function to use to get the current time (defaults to datetime.now)
    :return: A predicate that checks if the current time is before the given time
    """
    def predicate() -> bool:
        """
        :return: Whether the current time is before the given time
        """
        return now() < time
    predicate.__name__ = f'_{is_before.__name__}_{datetime}'
    return predicate


def is_not_implemented_yet() -> bool:
    """
    :return: False
    """
    return False


# Multi-args predicates
def is_greater_than_multi(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> bool:
    """
    :param a: A number
    :param b: A number
    :return: Whether a is greather than b
    """
    return a > b


def is_greater_than_or_equal_multi(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> bool:
    """
    :param a: A number
    :param b: A number
    :return: Whether a is greater than or equal to b
    """
    return a >= b


def is_less_than_multi(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> bool:
    """
    :param a: A number
    :param b: A number
    :return: Whether a is less than b
    """
    return a < b


def is_less_than_or_equal_multi(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> bool:
    """
    :param a: A number
    :param b: A number
    :return: Whether a is less than or equal to b
    """
    return a <= b
