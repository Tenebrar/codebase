from projecteuler.util.enumeration import enumerate_until
from projecteuler.util.sequences import fibonacci


def problem_0025(digits: int) -> int:
    minimum = 10 ** (digits - 1)

    return enumerate_until(lambda fib: fib >= minimum, fibonacci()) + 1  # Adjust for 0-indexing


if __name__ == '__main__':
    DIGITS = 1000

    print(problem_0025(DIGITS))
    # Expected: 4782
