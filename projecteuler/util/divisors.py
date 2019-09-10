from itertools import count, chain
from math import sqrt, log2
from typing import Iterable, Tuple

from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive


@precondition(0, is_strict_positive)
def prime_divisors(number: int) -> Iterable[int]:
    """ Returns the prime divisors of the number (sorted in ascending order). E.g. prime_divisors(20) -> 2, 2, 5 """
    for divisor in chain([2], count(3, step=2)):
        while number % divisor == 0:
            yield(divisor)
            number //= divisor

        if divisor > sqrt(number):
            break

    # If the original number was prime
    if number != 1:
        yield number


def divisor_pairs(number) -> Iterable[Tuple[int, int]]:
    """ Returns all divisors in pairs (including (1, number), and potentially (sqrt(number), sqrt(number))) """
    for x in range(1, int(sqrt(number)) + 1):
        if number % x == 0:
            yield x, number // x


def divisors(num: int) -> Iterable[int]:
    """ Returns the divisors of a number (no order is guaranteed) """
    for pair in divisor_pairs(num):
        yield pair[0]
        if pair[0] != pair[1]:
            yield pair[1]  # Avoid returning an exact sqrt twice


def num_divisors(num: int) -> int:
    """ Returns the number of divisors of a number """
    return sum(1 for _ in divisors(num))


def extract_exponent_of_two_divisor(num: int) -> int:
    """ Returns the exponent of the largest power of 2 that divides the input """
    # Based on https://www.geeksforgeeks.org/highest-power-of-two-that-divides-a-given-number/
    return int(log2(num & (~(num - 1))))
