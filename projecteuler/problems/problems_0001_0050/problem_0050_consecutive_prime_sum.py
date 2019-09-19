from projecteuler.util.timing import print_time
from util.primes import primes_until


def problem_0050(maximum: int) -> int:
    primes_list = list(primes_until(maximum))
    primes_set = set(primes_list)

    maximum_consecutive = 0
    p = 0

    for i in range(len(primes_list)):
        total = 0
        for j in range(i, len(primes_list)):
            total += primes_list[j]
            if total > maximum:
                break

            if total in primes_set and j - i > maximum_consecutive:
                maximum_consecutive = j - i
                p = total

    return p


if __name__ == '__main__':
    MAXIMUM = 1000000

    print(problem_0050(MAXIMUM))
    # Expected: 997651
