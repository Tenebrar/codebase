from numpy import zeros
from typing import Tuple

from advent_of_code.util import input_file


def parse_coordinate(string: str) -> Tuple[int, int]:
    s = string.split(', ')
    return int(s[0]), int(s[1])


with input_file() as file:
    coordinates = [parse_coordinate(line.rstrip('\n')) for line in file]


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


grid = zeros((400, 400), dtype=int)

for x in range(len(grid)):
    for y in range(len(grid[x])):
        for c in range(len(coordinates)):
            coordinate = coordinates[c]
            grid[x][y] += manhattan_distance(x, y, coordinate[0], coordinate[1])

MAX = 10000
count = 0
for row in grid:
    for value in row:
        if value < MAX:
            count += 1

print(count)
