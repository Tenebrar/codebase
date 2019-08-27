from itertools import count
from math import log2, sqrt

WANTED_NUMBER_OF_DIVISORS = 500


def num_divisors(num: int) -> int:
    """ Returns the number of divisors of a number """
    # Based on method 2 on https://www.quora.com/What-is-the-total-number-of-divisors-of-600 , method 1 was much slower
    result = 0
    for div in range(1, int(sqrt(num)) + 1):
        if num % div == 0:
            result += 2
        if div * div == num:
            result -= 1  # Avoid counting an exact sqrt twice

    return result


def extract_exponent_of_two_divisor(num: int) -> int:
    """ Returns the exponent of the largest power of 2 that divides the input """
    # Based on https://www.geeksforgeeks.org/highest-power-of-two-that-divides-a-given-number/
    return int(log2(num & (~(num - 1))))


# We use the formula for a triangular number to speed up our calculations
n = 1
divisors_n = num_divisors(n)
for n_plus_one in count(2):
    divisors_n_plus_one = num_divisors(n_plus_one)

    # One of n or (n+1) is odd anyway
    two_pow = extract_exponent_of_two_divisor(n) + extract_exponent_of_two_divisor(n_plus_one)

    # 2 consecutive numbers have no shared divisors, so the number of divisors of the product is the product of the
    # number of divisors
    # The calculation for the number of divisors for a number divided by 2 is based on method 1 from the above link
    divisors_triangle = divisors_n * divisors_n_plus_one // (two_pow + 1) * two_pow

    if divisors_triangle > WANTED_NUMBER_OF_DIVISORS:
        break

    n = n_plus_one
    divisors_n = divisors_n_plus_one

print(n * n_plus_one // 2)
# Expected: 76576500
