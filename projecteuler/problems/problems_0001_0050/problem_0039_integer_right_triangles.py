from typing import Tuple, Iterable

from projecteuler.util.divisors import divisor_pairs
from projecteuler.util.enumeration import enumerate_max
from util.conditions.decorators import precondition
from util.conditions.predicates import is_even


@precondition(0, is_even)  # All pythagorean triplets have an even sum
def _get_pythagorean_triples(total: int) -> Iterable[Tuple[int, int, int]]:
    """ Return all pythagorean triples that sum to the given value """
    # Based on problem 9
    for x, y in divisor_pairs(total * total // 2):
        a = total - y
        b = total - x

        c = total - a - b

        if a > 0 and b > 0 and c > 0:
            yield a, b, c


def problem_0039(maximum: int) -> int:
    return enumerate_max(lambda i: len(list(_get_pythagorean_triples(i))), range(2, maximum + 1, 2))


if __name__ == '__main__':
    MAXIMUM = 1000

    print(problem_0039(MAXIMUM))
    # Expected: 840
