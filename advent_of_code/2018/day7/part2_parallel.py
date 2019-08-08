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


def duration(char: str) -> int:
    return 61 + ord(char) - ord('A')


MAX_WORKERS = 5
time = 0
workers = []
while values:
    available = sorted(list(values.difference(requirements.keys())))
    while available and len(workers) < MAX_WORKERS:
        task = available.pop(0)
        values.remove(task)
        workers.append((time + duration(task), task))
    workers.sort()

    time, done = workers.pop(0)

    # print(f'Removing {done} at time {time}, workers: {workers}')
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
print(time)
