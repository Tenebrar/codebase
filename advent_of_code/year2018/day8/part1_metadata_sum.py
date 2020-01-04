from typing import List

from advent_of_code.util import input_file

with input_file() as file:
    nodes = [int(i) for i in file.read().rstrip('\n').split(' ')]


def sum_metadata(nodes: List[int]) -> int:
    children = nodes.pop(0)
    metadata = nodes.pop(0)

    sum = 0
    for i in range(children):
        sum += sum_metadata(nodes)

    for i in range(metadata):
        sum += nodes.pop(0)
    return sum


print(sum_metadata(nodes))
