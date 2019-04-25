from util.combinatorics.functions import (
    bell_number, binomial_coefficient, factorial, stirling_number_of_the_second_kind
)


def permutations(k: int) -> int:
    """
    Returns the number of permutations for an amount of items

    :param k: The number of items
    :return: The number of permutations for those items
    """
    return factorial(k)


def choose_distinct_elements_unordered(elements: int, choices: int):
    """
    Returns the number of ways to select `choices` different items from `elements` options without caring about the
    order in which they are picked

    :param elements: The number of items
    :param choices: The number of selected items
    :return: The number of ways to select k items from n options
    """
    return binomial_coefficient(elements, choices)


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
    Returns the number of ways you can partition items into non-empty subsets

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
