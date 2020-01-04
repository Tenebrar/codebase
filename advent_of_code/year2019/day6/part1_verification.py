from collections import defaultdict
from typing import Dict, List

from advent_of_code.util import input_file


def count_orbits(orbits: Dict[str, List[str]], start='COM', depth: int=1) -> int:
    return len(orbits[start]) * depth + sum(count_orbits(orbits, obj, depth + 1) for obj in orbits[start])


orbits = defaultdict(list)
with input_file() as file:
    for line in file:
        base, orbiter = line.strip().split(')')
        orbits[base].append(orbiter)


# Really hacky
from sys import setrecursionlimit
setrecursionlimit(2000)

print(count_orbits(orbits))

