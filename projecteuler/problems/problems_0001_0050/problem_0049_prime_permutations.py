from collections import defaultdict
from itertools import combinations

from util.primes import primes_until


def problem_0049() -> int:
    candidates = [prime for prime in primes_until(10000) if prime > 1000]

    map = defaultdict(list)
    for candidate in candidates:
        map[''.join(sorted(str(candidate)))].append(candidate)

    for grouping in map.values():
        for c in combinations(grouping, 3):
            if c == (1487, 4817, 8147):
                continue
            if c[1] - c[0] == c[2] - c[1]:
                return c[0] * 10**8 + c[1] * 10**4 + c[2]


if __name__ == '__main__':
    print(problem_0049())
    # Expected: 296962999629
