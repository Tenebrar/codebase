from projecteuler.util.divisors import prime_divisors
from util.conditions.decorators import precondition
from util.conditions.predicates import is_strict_positive


@precondition(0, is_strict_positive)
def problem_0003(number: int) -> int:
    return max(prime_divisors(number))


if __name__ == '__main__':
    NUMBER = 600851475143

    print(problem_0003(NUMBER))
    # Expected: 6857
