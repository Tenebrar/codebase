from itertools import combinations_with_replacement

from projecteuler.util.number_properties import is_abundant


def problem_0023(maximum: int) -> int:
    abundant_numbers = [i for i in range(1, maximum + 1) if is_abundant(i)]
    sums = {a + b for a, b in combinations_with_replacement(abundant_numbers, 2)}

    return sum(i for i in range(1, maximum + 1) if i not in sums)


if __name__ == '__main__':
    MAXIMUM = 28123

    print(problem_0023(MAXIMUM))
    # Expected: 4179871

# IDEA Maybe one of these properties can be leveraged for a better solution
# https://en.wikipedia.org/wiki/Abundant_number#Properties
# Properties of abundant numbers:
# - The smallest abundant number is 12
# - The smallest odd abundant number is 945
# - Every even integer greater than 46 can be written as the sum of 2 abundant numbers in at least 1 way
# - All multiples of an abundant number are also abundant
# - Every multiple (beyond 1) of a perfect number is abundant
