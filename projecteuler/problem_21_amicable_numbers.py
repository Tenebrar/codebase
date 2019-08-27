from math import sqrt
from typing import Iterable

MAXIMUM = 10000


def divisors(num: int) -> Iterable[int]:
    """ Returns the divisors of a number (no order is guaranteed) """
    result = {1}  # Using a set avoids adding an exact sqrt twice
    for div in range(2, int(sqrt(num)) + 1):
        if num % div == 0:
            result.add(div)
            result.add(num // div)

    return result


def is_amicable_number(num: int) -> bool:
    """ Returns whether the number is part of an amicable number pair """
    friend = sum(divisors(num))
    # Only those in pairs are amicable numbers. If the sum is the number itself, it's a perfect number
    return friend != num and sum(divisors(friend)) == num


print(sum(filter(is_amicable_number, range(1, MAXIMUM))))
# Expected: 31626
