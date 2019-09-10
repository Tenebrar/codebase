from itertools import combinations

from projecteuler.util.enumeration import digit_range
from projecteuler.util.number_properties import is_palindrome
from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive


@precondition(0, is_strict_positive)
def problem_0004(digits: int) -> int:
    return max(filter(is_palindrome, (x * y for (x, y) in combinations(digit_range(digits), 2))))


if __name__ == '__main__':
    DIGITS = 3

    print(problem_0004(DIGITS))
    # Expected: 906609
