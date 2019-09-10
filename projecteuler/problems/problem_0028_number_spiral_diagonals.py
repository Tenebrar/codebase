from projecteuler.util.summation import square_pyramidal_number, sum_all_to
from util.conditions.decorators import precondition
from util.conditions.predicates import is_odd


@precondition(0, is_odd)
def problem_0028(spiral_size: int) -> int:
    arm_length = (spiral_size - 1) // 2

    # Based on the formulas is https://oeis.org/A200975
    total = 1

    total += square_pyramidal_number(arm_length) * 8
    total += square_pyramidal_number(arm_length - 1) * 8

    total += sum_all_to(arm_length) * 6
    total += sum_all_to(arm_length - 1) * 14

    total += arm_length * 10

    return total


if __name__ == '__main__':
    SPIRAL_SIZE = 1001

    print(problem_0028(SPIRAL_SIZE))
    # Expected: 669171001
