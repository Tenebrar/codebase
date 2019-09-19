from functools import lru_cache
from itertools import count
from math import sqrt

from projecteuler.util.timing import print_time


@lru_cache(maxsize=None)  # minor speed gain with caching
def _pentagon(number: int) -> int:
    return number * (3 * number - 1) // 2


def _is_pentagon_number(number: int) -> bool:
    """ A number is a pentagonal number if there is a positive integer solution to its equation """
    x = (1 + sqrt(1 + 24 * number)) / 6
    return x == int(x)


def problem_0044() -> int:
    minimum = 2**100  # Technically, this is an assumption, but this one seems reasonable

    for index1 in count(1):  # Putting range(3000) here, will greatly speed this up, but that would be an assumption
        if _pentagon(index1) - _pentagon(index1 - 1) > minimum:
            break

        for index2 in range(index1 - 1, 0, -1):
            pent1 = _pentagon(index1)
            pent2 = _pentagon(index2)

            if pent1 - pent2 > minimum:
                break

            if _is_pentagon_number(pent1 - pent2) and _is_pentagon_number(pent1 + pent2):
                minimum = min(minimum, pent1 - pent2)

    return minimum


if __name__ == '__main__':
    with print_time():
        print(problem_0044())
        # Expected: 5482660

# IDEA Can I know more about the solution based on these formulae?
# n(3n-1)/2 + m(3m-1)/2 = l(3l-1)/2
# n(3n-1) + m(3m-1) = l(3l-1)
# 3n^2 - n + 3m^2 - m = 3l^2 - l

# 3n^2 - n - 3m^2 - m = 3k^2 - k

# a + b = c
# a - b = d

# 2b = c - d
# 2a = c + d
