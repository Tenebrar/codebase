from functools import reduce
from numpy.core._rational_tests import lcm


def problem_0005(maximum: int) -> int:
    return reduce(lcm, range(1, maximum))


if __name__ == '__main__':
    MAXIMUM = 20

    print(problem_0005(MAXIMUM))
    # Expected: 232792560
