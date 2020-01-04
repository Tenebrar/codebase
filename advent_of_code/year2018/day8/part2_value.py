from typing import List

from advent_of_code.util import input_file

with input_file() as file:
    nodes = [int(i) for i in file.read().rstrip('\n').split(' ')]


def value(nodes: List[int]) -> int:
    children = nodes.pop(0)
    metadata = nodes.pop(0)

    if not children:
        sum = 0
        for i in range(metadata):
            sum += nodes.pop(0)
        return sum

    child_values = []
    for i in range(children):
        child_values.append(value(nodes))

    sum = 0
    for i in range(metadata):
        child_index = nodes.pop(0) - 1
        if 0 <= child_index < len(child_values):
            sum += child_values[child_index]

    return sum


print(value(nodes))
