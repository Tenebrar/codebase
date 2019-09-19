from itertools import count

from projecteuler.util.divisors import prime_divisors
from projecteuler.util.timing import print_time


def problem_0047(amount: int) -> int:
    consecutive = 0
    for i in count(2):
        if len(set(prime_divisors(i))) == amount:  # The assignment is unclear on == or >=, but results are the same
            consecutive += 1

            if consecutive == amount:
                return i - amount + 1
        else:
            consecutive = 0


if __name__ == '__main__':
    with print_time():
        AMOUNT = 4

        print(problem_0047(AMOUNT))
        # Expected: 134043
