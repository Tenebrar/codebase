from collections import defaultdict
from re import search
from typing import Tuple

from advent_of_code.util import input_file


def parse_order(string: str) -> Tuple[str, str]:
    match = search('^Step (.) must be finished before step (.) can begin\.\n$', string)
    return match.group(1), match.group(2)


with input_file() as file:
    orders = [parse_order(line) for line in file]

values = set()
requirements = defaultdict(set)
for order in orders:
    values.add(order[0])
    values.add(order[1])
    requirements[order[1]].add(order[0])

while values:
    done = sorted(list(values.difference(requirements.keys())))[0]
    values.remove(done)
    removable = []
    for key, value in requirements.items():
        try:
            value.remove(done)
            if not value:
                removable.append(key)
        except KeyError:
            pass
    for key in removable:
        del requirements[key]
    print(done, end='')
print()
