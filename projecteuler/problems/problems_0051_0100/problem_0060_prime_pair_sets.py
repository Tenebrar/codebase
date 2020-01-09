from itertools import combinations
from typing import Tuple, List, Dict, Set

from projecteuler.util.timing import print_time
from util.primes import primes_until, is_prime

PRIMES = list(primes_until(10000))  # TODO remove list, if only iterated once


def _is_prime_pair(prime1: int, prime2: int) -> bool:
    if not is_prime(int(str(prime1) + str(prime2))):
        return False
    if not is_prime(int(str(prime2) + str(prime1))):
        return False
    return True


def problem_0060(set_size: int) -> int:
    cliques: Set[frozenset] = set()

    for primes in combinations(PRIMES, 2):
        if _is_prime_pair(*primes):
            cliques.add(frozenset(primes))

    print(2, cliques)

    for size in range(3, set_size + 1):
        new_cliques: Set[frozenset] = set()
        for clique1, clique2 in combinations(cliques, 2):
            c = clique1.symmetric_difference(clique2)
            if len(c) == 2 and _is_prime_pair(*c):
                new_cliques.add(frozenset(clique1.union(c)))

        cliques = new_cliques
        print(size, cliques)


    pairs: Dict[int, List[int]] = {}
    for prime in PRIMES:
        matches = []
        for pair_candidate in pairs:
            if _is_prime_pair(prime, pair_candidate):
                pairs[pair_candidate].append(prime)
                matches.append(pair_candidate)

        pairs[prime] = matches

    print(pairs)


if __name__ == '__main__':
    with print_time():
        SET_SIZE = 5

        print(problem_0060(SET_SIZE))
        # Expected:
