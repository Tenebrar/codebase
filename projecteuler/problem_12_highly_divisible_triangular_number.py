from itertools import count, dropwhile
from math import sqrt

WANTED_NUMBER_OF_DIVISORS = 500


def triangular_number(i: int) -> int:
    return i * (i + 1) // 2


def num_divisors(i: int) -> int:
    # Based on method 2 on https://www.quora.com/What-is-the-total-number-of-divisors-of-600 , method 1 was much slower
    result = 0
    for div in range(1, int(sqrt(i)) + 1):
        if i % div == 0:
            result += 2
        if div * div == i:
            result -= 1  # Avoid counting an exact sqrt twice

    return result


print(next(dropwhile(lambda x: num_divisors(x) <= WANTED_NUMBER_OF_DIVISORS, map(triangular_number, count(1)))))
# Expected: 76576500

# IDEA: I should be able to take the num_divisors of n and (n+1) and use those
