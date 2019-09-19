from typing import Set

PRIMES = [2, 3, 5, 7, 11, 13, 17]


def _try_permutations(current: str='', options: Set[str]=set(map(str, range(10)))) -> int:
    """ Try all permutations of 0-9, but stop as soon as a condition can no longer be met """
    if len(current) >= 4  and int(current[len(current) - 3:]) % PRIMES[len(current) - 4] != 0:
        return 0

    if not options:
        return int(current)

    return sum(_try_permutations(current + option, options - set(option)) for option in options)


def problem_0043() -> int:
    return _try_permutations()


if __name__ == '__main__':
    print(problem_0043())
    # Expected: 16695334890

# It is easier to work with strings than with ints, because it is ill-defined how a pandigital number starting with 0
# should work (Which numbers have the indices indicated).
