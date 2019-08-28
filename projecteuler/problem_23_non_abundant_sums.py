from itertools import combinations_with_replacement
from math import sqrt
from typing import Iterable

MAXIMUM = 28123


def divisors(num: int) -> Iterable[int]:
    """ Returns the divisors of a number (no order is guaranteed) """
    result = {1}  # Using a set avoids adding an exact sqrt twice
    for div in range(2, int(sqrt(num)) + 1):
        if num % div == 0:
            result.add(div)
            result.add(num // div)

    return result


def is_abundant_number(num: int) -> bool:
    """ Returns whether the number is abundant """
    return sum(divisors(num)) > num


abundant_numbers = [i for i in range(1, MAXIMUM + 1) if is_abundant_number(i)]
sums = {a + b for a, b in combinations_with_replacement(abundant_numbers, 2)}

print(sum(i for i in range(1, MAXIMUM + 1) if i not in sums))
# Expected: 4179871

# IDEA Maybe one of these properties can be leveraged for a better solution
# https://en.wikipedia.org/wiki/Abundant_number#Properties
# Properties of abundant numbers:
# - The smallest abundant number is 12
# - The smallest odd abundant number is 945
# - Every even integer greater than 46 can be written as the sum of 2 abundant numbers in at least 1 way
# - All multiples of an abundant number are also abundant
# - Every multiple (beyond 1) of a perfect number is abundant
