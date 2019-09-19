from itertools import count
from math import sqrt


def _triangle(index: int) -> int:
    return index * (index + 1) // 2


def _is_triangle_number(number: int) -> bool:
    # Use the formula (-b + sqrt(b^2 -4ac)) / 2a to solve x^2 + x - 2*number == 0 (we only want positive results)
    x = (-1 + sqrt(1 + 8 * number)) / 2
    return x == int(x)


def _pentagonal(index: int) -> int:
    return index * (3 * index - 1) // 2


def _is_pentagon_number(number: int) -> bool:
    # Use the formula (-b + sqrt(b^2 -4ac)) / 2a to solve 3x^2 - x - 2*number == 0 (we only want positive results)
    x = (1 + sqrt(1 + 24 * number)) / 6
    return x == int(x)


def _hexagonal(index: int) -> int:
    return index * (2 * index - 1)


def _is_hexagon_number(number: int) -> bool:
    # Use the formula (-b + sqrt(b^2 -4ac)) / 2a to solve 2x^2 - x - number == 0 (we only want positive results)
    x = (1 + sqrt(1 + 8 * number)) / 4
    return x == int(x)


def problem_0045() -> int:
    # Start after the given number
    for index in count(144):
        i = _hexagonal(index)
        if _is_pentagon_number(i) and _is_triangle_number(i):
            return i


if __name__ == '__main__':
    print(problem_0045())
    # Expected: 1533776805
