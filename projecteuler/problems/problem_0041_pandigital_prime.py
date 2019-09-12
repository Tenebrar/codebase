from functools import reduce
from itertools import permutations
from typing import Iterable

from util.primes import is_prime


def _digits_to_number(digits: Iterable[int]) -> int:
    """ Gives the number given by its digits, e.g. [1, 2, 3] -> 123 """
    return reduce(lambda x, y: x * 10 + y, digits)


def problem_0041() -> int:
    for digits in range(9, 0, -1):
        permuted_digits = permutations(range(1, digits + 1))
        pandigital_numbers = map(_digits_to_number, permuted_digits)
        maximum = max(filter(is_prime, pandigital_numbers), default=0)

        if maximum:
            return maximum


if __name__ == '__main__':
    print(problem_0041())
    # Expected: 7652413
