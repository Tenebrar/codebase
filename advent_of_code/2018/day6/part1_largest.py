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


TIE = -1
grid = zeros((400, 400), dtype=int)

for x in range(len(grid)):
    for y in range(len(grid[x])):
        min_dist = 1000000
        for c in range(len(coordinates)):
            coordinate = coordinates[c]
            dist = manhattan_distance(x, y, coordinate[0], coordinate[1])
            if dist < min_dist:
                min_dist = dist
                grid[x][y] = c
            elif dist == min_dist:
                grid[x][y] = TIE

infinites = set()
for y in range(len(grid[0])):
    infinites.add(grid[0][y])
    infinites.add(grid[-1][y])
for x in range(len(grid)):
    infinites.add(grid[x][0])
    infinites.add(grid[x][-1])

counts = {}
for row in grid:
    for value in row:
        try:
            counts[value] += 1
        except KeyError:
            counts[value] = 1

for inf in infinites:
    del counts[inf]

print(sorted(counts.values(), reverse=True)[0])
