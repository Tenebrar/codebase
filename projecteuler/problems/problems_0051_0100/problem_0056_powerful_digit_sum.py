from typing import Iterable


def _digits(number: int) -> Iterable[int]:
    """ Return the digits of a number (in reverse order) """
    while number > 0:
        number, remainder = divmod(number, 10)
        yield remainder


def problem_0056(maximum: int) -> int:
    return max(sum(_digits(a ** b)) for a in range(1, maximum) for b in range(1, maximum))


if __name__ == '__main__':
    MAXIMUM = 100

    print(problem_0056(MAXIMUM))
    # Expected: 972
