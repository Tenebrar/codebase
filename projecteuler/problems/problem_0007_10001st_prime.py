from itertools import islice

from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive
from util.primes import primes


@precondition(0, is_strict_positive)
def problem_0007(index: int) -> int:
    return next(islice(primes(), index - 1, index))  # Adjust for 0-indexing


if __name__ == '__main__':
    INDEX = 10001

    print(problem_0007(INDEX))
    # Expected: 104743
