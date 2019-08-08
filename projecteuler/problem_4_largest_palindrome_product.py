from itertools import combinations
from typing import Iterable

DIGITS = 3


def digit_range(num_digits: int) -> Iterable[int]:
    """ Range over all numbers with a given number of digits """
    minimum = 10 ** (num_digits - 1)
    maximum = 10 ** num_digits
    return range(minimum, maximum)


def is_palindrome(number: int) -> bool:
    """ Returns whether a number is a palindrome """
    return str(number) == str(number)[::-1]


print(max(filter(is_palindrome, (x * y for (x, y) in combinations(digit_range(DIGITS), 2)))))
# Expected: 906609
