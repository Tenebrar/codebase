from itertools import chain, count
from math import sqrt
from random import randrange, getrandbits
from typing import Iterable


def is_prime(number):
    """ Returns whether the passed integer is a prime number """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    if number == 3:
        return True
    for j in range(3, int(sqrt(number)) + 1, 2):
        if number % j == 0:
            return False
    return True


def is_probable_prime(potential_prime, tests=100):
    """
    Perform a Miller-Rabin primality test

    :param potential_prime: The value to be tested
    :param tests: The amount of tests to perform
    :return: False if definitely not a prime, True if probable prime
    """
    if potential_prime <= 1:
        return False
    if potential_prime <= 3:
        # We need to handle some start values, since the algorithm only works after these
        return True
    if not potential_prime & 1:
        return False

    # We know possible_prime - 1 is even
    exponent, factor = extract_power_of_two(potential_prime - 1)

    for _ in range(tests):
        # Select a potential witness at random
        potential_witness = randrange(2, potential_prime - 2)
        if _is_composite(potential_witness, exponent, factor, potential_prime):
            return False
    return True


def extract_power_of_two(number):
    """
    Factorise the given number into a power of 2 and an odd number

    Example: extract_power_of_two(220) == 2, 55
    because 2**2 * 55 == 220, and 55 is odd

    :param number: The number to have a power of 2 extracted
    :return: a tuple containing the exponent and the remaining factor (which will be odd)
    """
    exponent = 0
    while not number & 1:
        exponent += 1
        number >>= 1
    return exponent, number


def _is_composite(potential_witness, exponent, factor, potential_prime):
    """
    Check if potential_prime is composite with regards to potential_witness

    For all primes p > 2, p - 1 is even and we can write that as (p - 1 == 2**e * f)
    For every value w, the following is true:
    w**f == 1 mod p
    or
    there exists an r (0 <= r <= s-1), for which w**((2**r * f) == -1 mod p

    So if we can find a witness, where this does not hold, we know the input is not prime

    :param potential_witness: The potential witness for the compositeness of the potential_prime
    :param exponent: 2**exponent * factor == potential_prime - 1
    :param factor: 2**exponent * factor == potential_prime - 1
    :param potential_prime: The potential prime to be tested
    :return: True if the potential_witness is an actual witness for the compositeness of the potential_prime
    """
    x = pow(potential_witness, factor, potential_prime)
    if x == 1 or x == potential_prime - 1:
        return False
    for i in range(exponent):
        x = pow(x, 2, potential_prime)
        if x == potential_prime - 1:
            return False
    return True


def get_probable_prime(num_bits):
    """
    Get an n-bit probable prime
    There is currently no guarantee that the number has any minimum value (other than 0), though that could be added;

    :param num_bits: The amount of bits desired
    :return: A number of num_bits bits that is probably prime
    """
    if num_bits <= 1:  # A number of 1 bit does not have a possible solution
        raise ValueError('Minimum number of bits is 2')

    while True:
        p = getrandbits(num_bits)
        if is_probable_prime(p):
            return p


def primes() -> Iterable[int]:
    """ An, admittedly not very efficient, way of generating all primes (without a known maximum) """
    return chain([2], filter(is_prime, count(3, 2)))


def primes_until(maximum: int) -> Iterable[int]:
    # Sieve of Eratosthenes is much faster if you need all primes to a given number
    candidates = [i for i in range(maximum + 1)]

    for candidate in candidates:  # candidates list changes during iteration, changed elements are returned
        if candidate > 1:
            yield candidate
            # Cross out the multiples of this prime
            for i in range(2, maximum // candidate + 1):
                candidates[i * candidate] = 0
