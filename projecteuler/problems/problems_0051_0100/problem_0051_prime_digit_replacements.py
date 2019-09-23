from itertools import combinations, count
from typing import Callable, Iterable, List, Tuple

from projecteuler.util.timing import print_time
from util.primes import primes_until

DIGIT_STRINGS = list(map(str, range(10)))


def _get_primes_of_length(digits: int) -> Tuple[List[int], Callable[[int], bool]]:
    """
    Return the primes with a given number of digits
    :param digits: the number of digits the primes should have
    :return: A list of primes, and a function for determining membership
    """
    # Sorted list for iteration
    sorted_primes = [prime for prime in primes_until(10 ** digits) if prime > 10 ** (digits - 1)]
    # Set for faster containment checking (faster even than binary search)
    primes_set = set(sorted_primes)
    return sorted_primes, lambda x: x in primes_set


def _wildcard_indices(digits: int, prime: int) -> Iterable[Tuple[int, ...]]:
    """
    Given a prime, determines the possible locations of "wildcards": places where the number has the same digits, which
    when replaced might give rise to more primes

    :param digits: The number of digits of the prime
    :param prime: The prime we're determining wildcards for
    :return: A generator of wildcard position
    """
    for wildcards in range(1, digits + 1):
        for combination in combinations(range(digits), wildcards):
            prime_string = str(prime)
            value = prime_string[combination[0]]
            same = all(prime_string[index] == value for index in combination)
            if same:  # Only those whose original positions on the wildcards are the same
                yield combination


def _options(prime: int, wilcard_indices: Tuple[int, ...]) -> Iterable[int]:
    """
    :param prime: A prime
    :param wilcard_indices: A number of positions where replacement can happen
    :return: A generator that returns all numbers with the wildcards replaced with the digits 0-9
    """
    prime_list = list(str(prime))
    for i in DIGIT_STRINGS:
        for index in wilcard_indices:
            prime_list[index] = i
        yield int(''.join(prime_list))


def problem_0051(family_size: int) -> int:
    for digits in count(2):
        sorted_primes, prime_check = _get_primes_of_length(digits)

        for prime in sorted_primes:
            for wildcard_indices in _wildcard_indices(digits, prime):
                size = sum(1 for option in _options(prime, wildcard_indices) if prime_check(option))
                if size >= family_size:
                    return next(option for option in _options(prime, wildcard_indices) if prime_check(option))


if __name__ == '__main__':
    with print_time():
        FAMILY_SIZE = 8

        print(problem_0051(FAMILY_SIZE))
        # Expected: 121313
