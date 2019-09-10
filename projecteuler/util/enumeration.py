from typing import Callable, Iterable, TypeVar, List, Any, Tuple

from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive

X = TypeVar('X')


def enumerate_max(mapping: Callable[[X], int], inputs: Iterable[X]) -> int:
    """ Returns the input that results in the largest result from the range of inputs """
    return max(((i, mapping(i)) for i in inputs), key=lambda x: x[1])[0]


def enumerate_until(predicate: Callable[[Any], bool], inputs: Iterable[Any]):
    for index, value in enumerate(inputs):
        if predicate(value):
            return index


@precondition(0, is_strict_positive)
def digit_range(num_digits: int) -> Iterable[int]:
    """ Range over all numbers with a given number of digits """
    minimum = 10 ** (num_digits - 1)
    maximum = 10 ** num_digits
    return range(minimum, maximum)


def overlapping_substrings(string: str, size: int) -> Iterable[str]:
    """ Yields all substrings of a given length from a string """
    for i in range(len(string) + 1 - size):
        yield string[i:i+size]


def grid_coordinates(grid: List[List[Any]]) -> Iterable[Tuple[int, int]]:
    """ Given a grid (2-dimensional list), iterate over all coordinates in it """
    height = len(grid)
    width = len(grid[0])

    for row in range(height):
        for column in range(width):
            yield row, column
