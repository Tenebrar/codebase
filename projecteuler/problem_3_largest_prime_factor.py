from math import sqrt

NUMBER = 600851475143


def prime_divisors(number):
    for i in range(2, int(sqrt(number)) + 1):
        while number % i == 0:
            yield(i)
            number //= i
    # If the original number was prime
    if number != 1:
        yield number


print(max(prime_divisors(NUMBER)))
# Expected: 6857
