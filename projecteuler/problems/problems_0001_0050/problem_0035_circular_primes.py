from typing import Iterable

from util.primes import primes_until


def _rotations(number: int) -> Iterable[int]:
    """ Returns the rotations of a number (excluding itself) """
    number_string = str(number)

    for index in range(1, len(number_string)):
        yield int(number_string[index:] + number_string[0:index])


def problem_0035(maximum: int) -> int:
    candidates = set(primes_until(maximum))

    return sum(1 for candidate in candidates if all(rotation in candidates for rotation in _rotations(candidate)))


if __name__ == '__main__':
    MAXIMUM = 1000000

    print(problem_0035(MAXIMUM))
    # Expected: 55
