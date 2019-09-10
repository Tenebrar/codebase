from functools import partial

from projecteuler.util.summation import sum_all_to
from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive


@precondition([0, 1], is_strict_positive)
def _sum_multiples_of(value: int, maximum: int) -> int:
    """
    Returns the sum of all multiples of value that are less than the maximum

    :param value: A value
    :param maximum: The maximum (exclusive)
    :return: The sum of all multiples of value that are less than the maximum
    """
    amount = (maximum - 1) // value
    return sum_all_to(amount) * value


@precondition([0, 1, 2], is_strict_positive)
def problem_0001(maximum: int, input1: int, input2: int) -> int:
    sum_multiples = partial(_sum_multiples_of, maximum=maximum)
    # Add both sums, and remove those that were counted double
    return sum_multiples(input1) + sum_multiples(input2) - sum_multiples(input1 * input2)


if __name__ == '__main__':
    MAXIMUM = 1000
    INPUT1 = 3
    INPUT2 = 5

    print(problem_0001(MAXIMUM, INPUT1, INPUT2))
    # Expected: 233168
