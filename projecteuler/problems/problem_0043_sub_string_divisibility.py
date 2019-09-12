from functools import reduce
from itertools import permutations
from typing import Iterable


def _digits_to_number(digits: Iterable[int]) -> int:
    """ Gives the number given by its digits, e.g. [1, 2, 3] -> 123 """
    return reduce(lambda x, y: x * 10 + y, digits)


def problem_0043() -> int:
    permuted_digits = permutations(range(10))
    pandigital_numbers = map(_digits_to_number, permuted_digits)

    total = 0
    for p in pandigital_numbers:
        print(p)
        total += 1
    print(total)


if __name__ == '__main__':
    print(problem_0043())
