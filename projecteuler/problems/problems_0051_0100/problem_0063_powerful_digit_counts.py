from itertools import count
from math import log10


def _number_of_digits(number: int) -> int:
    """ Returns the number of digits in the given number """
    return int(log10(number)) + 1


def problem_0063() -> int:
    result = 0  # No need to save the numbers, duplicates are not possible

    for n in count(1):
        if _number_of_digits(9 ** n) < n:
            break  # If the requested length is not reached anymore, we can stop

        for i in range(1, 10):  # This will never be >= 10, as 10 ** n has n+1 digits
            if _number_of_digits(i ** n) == n:
                result += 1

    return result


if __name__ == '__main__':
    print(problem_0063())
    # Expected: 49
