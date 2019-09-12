from itertools import chain
from typing import Iterable, Callable

from util.conditions.predicates import is_in
from util.primes import primes_until
from math import log10


def _left(number: int) -> Iterable[int]:
    """ Returns the numbers gotten by truncating the input from left to right """
    divisor = (10 ** int(log10(number)))
    number %= divisor

    divisor //= 10
    while divisor != 0:
        yield number
        number %= divisor
        divisor //= 10


def _right(number: int) -> Iterable[int]:
    """ Returns the numbers gotten by truncating the input from right to left """
    number //= 10
    while number != 0:
        yield number
        number //= 10


def _is_truncatable(prime: int, is_prime: Callable[[int], bool]) -> bool:
    """
    :param prime: A prime number
    :param is_prime: A function to use to check primality
    :return: Whether the prime is left and right truncatable prime
    """
    if prime < 10:  # Eulerproject does not count single digit primes as truncatable
        return False

    return all(map(is_prime, chain(_left(prime), _right(prime))))


def problem_0037():
    primes = set(primes_until(1000000))
    is_prime = is_in(primes)

    return sum(prime for prime in primes if _is_truncatable(prime, is_prime))


if __name__ == '__main__':
    print(problem_0037())
    # Expected: 748317

# IDEA I currently use a MAXIMUM of 1 million (and I could verify I have 11),
# but I should be able to show this limit somehow

# We could simply look them up, but that would be cheating :)
# https://oeis.org/A020994
# print(sum([23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]))
