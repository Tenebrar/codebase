from itertools import count, chain, islice
from typing import Iterable

from util.primes import is_prime

INDEX = 10001
INDEX -= 1  # Adjust for 0-indexing


def primes() -> Iterable[int]:
    """ An, admittedly not very efficient, way of generating all primes """
    return chain([2], filter(is_prime, count(3, 2)))


print(next(islice(primes(), INDEX, INDEX + 1)))
