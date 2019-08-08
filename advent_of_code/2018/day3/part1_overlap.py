from numpy import zeros
from re import search
from typing import Tuple

from advent_of_code.util import input_file


def parse_claim(string: str) -> Tuple[int, int, int, int]:
    match = search('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)\n$', string)
    return int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5))


with input_file() as file:
    claims = [parse_claim(line) for line in file]

cloth = zeros((1000, 1000), dtype=int)

for x, y, width, height in claims:
    for i in range(width):
        for j in range(height):
            cloth[x + i][y + j] += 1

count = 0
for row in cloth:
    for value in row:
        if value > 1:
            count += 1

print(count)
