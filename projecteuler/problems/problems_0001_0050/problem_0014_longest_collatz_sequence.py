from functools import lru_cache

from projecteuler.util.enumeration import enumerate_max


@lru_cache(maxsize=None)
def collatz_sequence_length(num: int) -> int:
    """ Returns the length of the Collatz sequence starting at a given number """
    if num == 1:
        return 1

    if num % 2 == 0:
        return collatz_sequence_length(num // 2) + 1
    else:
        return collatz_sequence_length(3 * num + 1) + 1


def problem_0014(max_starting_number: int) -> int:
    return enumerate_max(collatz_sequence_length, range(1, max_starting_number))


if __name__ == '__main__':
    MAX_STARTING_NUMBER = 1000000

    print(problem_0014(MAX_STARTING_NUMBER))
    # Expected: 837799
