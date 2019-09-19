from typing import List

from projecteuler.util.permutations import permutation


def problem_0024(number: int, elements: List[int]) -> int:
    return int(''.join(str(i) for i in permutation(number, elements)))


if __name__ == '__main__':
    PERMUTATION = 1000000
    ELEMENTS = [i for i in range(10)]

    print(problem_0024(PERMUTATION, ELEMENTS))
    # Expected: 2783915460
