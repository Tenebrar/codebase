from typing import Callable, NamedTuple

from util.combinatorics.functions import (
    bell_number, binomial_coefficient, factorial, falling_factorial, stirling_number_of_the_second_kind
)


def permutations(k: int) -> int:
    """
    Returns the number of permutations for an amount of items

    :param k: The number of items
    :return: The number of permutations for those items
    """
    return factorial(k)


class Choose:
    """
    Class that groups the ways of choosing elements from a set:
    - distinct or with repetition (whether the chosen elements will be unique)
    - ordered or unordered (whether a-b and b-a are considered the same option)

    E.g. Choose.distinct.ordered(5, 3)
    """
    class _Ordering(NamedTuple):
        """Helper class"""
        ordered: Callable[[int, int], int]
        unordered: Callable[[int, int], int]

    # Can be seen as permutations with the first 'choices' elements being chosen
    distinct = _Ordering(
        # Permute all elements, remove all permutations of not chosen elements
        ordered=lambda elements, choices: falling_factorial(elements, choices),
        # Permute all elements, remove all permutations of not chosen elements and those of chosen elements
        unordered=lambda elements, choices: binomial_coefficient(elements, choices)
    )
    # Allow repeated results
    with_repetition = _Ordering(
        # 'Elements' options for each choice
        ordered=lambda elements, choices: elements ** choices,
        # Can be considered choosing elements from a set that also has (repeat element 1, repeat element 2,...)
        unordered=lambda elements, choices: binomial_coefficient(elements + choices - 1, choices)
    )


def lattice_paths(a: int, b: int):
    """
    Returns the number of lattice paths from the origin (0,0) to a point (a,b) of length a+b.
    The length requirements restricts the paths to only allowing 2 cardinal directions.

    A lattice path is a path composed of connected horizontal and vertical line segments, each passing between adjacent
    lattice points.

    Can be seen as choosing `a` elements out of a path of length `a+b` to be the ones that go in a certain direction.

    In the explanation, a and b are assumed to be positive. The function will take their absolute values

    :param a: an integer
    :param b: an integer
    :return: the number of lattice paths from (0,0) to (a,b) of length a+b
    """
    return binomial_coefficient(abs(a) + abs(b), abs(a))


def partition_non_empty(items: int, subsets: int) -> int:
    """
    Returns the number of ways you can partition items into a fixed amount of non-empty subsets

    :param items: The number of items
    :param subsets: The desired number of no-empty subsets
    :return: the number of ways you can partition items into non-empty subsets
    """
    return stirling_number_of_the_second_kind(items, subsets)


def partitions(items: int) -> int:
    """
    Returns the number of ways a set of elements can be partitioned

    :param items: The number of items
    :return: The number of ways a set of elements can be partitioned
    """
    return bell_number(items)
