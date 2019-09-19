from itertools import count
from math import factorial


def _is_digit_factorial(number: int) -> bool:
    """ Returns whether a number is equal to the sum of the factorial of its digits """
    return sum(map(factorial, map(int, str(number)))) == number


def _find_max() -> int:
    """ Find a theoretical maximum where a number can be equal to the sum of the factorial of its digits """
    for digits in count(1):
        maximum = 10 ** digits - 1
        value = factorial(9) * digits

        if maximum > value:
            return value


def problem_0034() -> int:
    return sum(i for i in range(10, _find_max()) if _is_digit_factorial(i))


if __name__ == '__main__':
    print(problem_0034())
    # Expected: 40730


# IDEA I have no real idea why this is so slow
# caching the factorial call and improving the digit mapping had no effect
# maybe an interesting one to profile at some point?
# I could cache some sums and only add new digits?
