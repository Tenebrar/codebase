from typing import Iterable

from hacker.primes import is_probable_prime
from hacker.settings import inputfile

filename = inputfile('coding', 'primal_pi', 'pi1000000.txt')

with open(filename, 'r') as file:
    pi = file.read().strip()

length = 2048
piece_of_pi = pi[2:2+length]


def overlapping_substrings(string: str, size: int) -> Iterable[str]:
    """ Yields all substrings of a given length from a string """
    for i in range(len(string) + 1 - size):
        yield string[i:i+size]


prime = None
while not prime:
    print(f'checking length {length}')
    for s in overlapping_substrings(piece_of_pi, length):
        if is_probable_prime(int(s)):
            prime = s
            break
    length -= 1

print(prime)
