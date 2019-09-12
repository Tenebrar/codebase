from typing import Iterable

from projecteuler.util.operators import product


def problem_0040(indices: Iterable[int]) -> int:
    constant = ''.join(str(i) for i in range(0, max(indices)))

    return product(int(constant[i]) for i in indices)


if __name__ == '__main__':
    INDICES = [1, 10, 100, 1000, 10000, 100000, 1000000]

    print(problem_0040(INDICES))
    # Expected: 210

# IDEA I should probably be able to find a formula to calculate these, but this solution is so easy
