from functools import partial

from projecteuler.util.enumeration import enumerate_max


def long_division_cycle(dividend: int, divisor: int, prev=None) -> int:
    """ Returns the length of the cycle of repeating digits when dividing dividend by divisor """
    prev = prev or []

    while True:
        if dividend in prev:
            return len(prev) - prev.index(dividend)

        prev.append(dividend)
        dividend = dividend % divisor * 10


def problem_0026(max_divisor: int) -> int:
    return enumerate_max(partial(long_division_cycle, 1), range(1, max_divisor))


if __name__ == '__main__':
    MAX_DIVISOR = 1000

    print(problem_0026(MAX_DIVISOR))
    # Expected: 983
