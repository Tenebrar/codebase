from itertools import islice
from math import log10
from typing import Tuple, Iterable


def _expansions() -> Iterable[Tuple[int, int]]:
    numerator, denominator = 3, 2
    while True:
        yield numerator, denominator

        old_denominator = denominator
        denominator += numerator
        numerator = denominator + old_denominator


def _is_valid(expansion: Tuple[int, int]) -> bool:
    return int(log10(expansion[0])) > int(log10(expansion[1]))


def problem_0057(expansions: int) -> int:
    return sum(1 for expansion in islice(_expansions(), expansions) if _is_valid(expansion))


if __name__ == '__main__':
    EXPANSIONS = 1000

    print(problem_0057(EXPANSIONS))
    # Expected: 153
