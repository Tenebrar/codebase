from typing import Iterable

from projecteuler.util.timing import print_time
from util.primes import is_prime


# Again, based on the formulas in https://oeis.org/A200975 (though reworked so index 0 always gives result 1)
def _first_spiral_arm(n: int) -> int:
    return 4 * n * n - 2 * n + 1


def _second_spiral_arm(n: int) -> int:
    return 4 * n * n + 1


def _third_spiral_arm(n: int) -> int:
    return 4 * n * n + 2 * n + 1


def _fourth_spiral_arm(n: int) -> int:
    return 4 * n * n + 4 * n + 1


def _ratios() -> Iterable[float]:
    """ Returns the ratios of prime numbers on the diagonals of the Ulam spiral """
    index = 0
    primes = 0

    while True:
        primes += 1 if is_prime(_first_spiral_arm(index)) else 0
        primes += 1 if is_prime(_second_spiral_arm(index)) else 0
        primes += 1 if is_prime(_third_spiral_arm(index)) else 0
        primes += 1 if is_prime(_fourth_spiral_arm(index)) else 0

        yield primes / (index * 4 + 1)

        index += 1


def problem_0058(desired_ratio: float) -> int:
    for index, ratio in enumerate(_ratios()):
        if 0 < ratio < desired_ratio:  # Compare to 0 to prevent stopping at side length 1
            return index * 2 + 1


if __name__ == '__main__':
    with print_time():
        DESIRED_RATIO = 0.1

        print(problem_0058(DESIRED_RATIO))
        # Expected: 26241
