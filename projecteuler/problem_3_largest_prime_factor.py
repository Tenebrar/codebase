from math import sqrt

from util.primes import is_prime

# For a number in this range, this approach is more than sufficient

NUMBER = 600851475143

print(next(filter(is_prime, filter(lambda x: NUMBER % x == 0, range(int(sqrt(NUMBER)) + 1, 0, -1)))))
# Expected: 6857
