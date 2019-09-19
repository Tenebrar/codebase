from itertools import count
from typing import Iterable

from util.primes import is_prime


def _squares() -> Iterable[int]:
    return (i * i for i in count(1))


def _double(iterable: Iterable[int]) -> Iterable[int]:
    return (2 * i for i in iterable)


def _test_number(number: int) -> bool:
    """ Check whether the number upholds the conjecture """
    for s in _double(_squares()):
        if s >= number:
            return False
        if is_prime(number - s):
            return True


def problem_0046() -> int:
    for i in count(3, 2):
        if not is_prime(i) and not _test_number(i):
            return i


if __name__ == '__main__':
    print(problem_0046())
    # Expected: 5777
