from itertools import takewhile

from projecteuler.util.sequences import fibonacci
from util.conditions.predicates import is_even, is_less_than


def problem_0002(maximum: int) -> int:
    return sum(filter(is_even, takewhile(is_less_than(maximum), fibonacci())))


if __name__ == '__main__':
    MAXIMUM = 4000000

    print(problem_0002(MAXIMUM))
    # Expected: 4613732

# The golden ratio approximation could have been used, but I felt these numbers were too small to warrant it

# The sequence has a repeating pattern of 'odd, odd, even', but there seems to be no real way of using that
# It could avoid the modulo check for evenness, but it's not like that is such a heavy operation anyway
