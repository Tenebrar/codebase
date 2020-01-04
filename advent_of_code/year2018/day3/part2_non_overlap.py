from numpy import zeros
from re import search
from typing import Tuple

from advent_of_code.util import input_file


def parse_claim(string: str) -> Tuple[int, int, int, int, int]:
    match = search('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)\n$', string)
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5))


with input_file() as file:
    claims = [parse_claim(line) for line in file]

cloth = zeros((1000, 1000), dtype=int)

for _, x, y, width, height in claims:
    for i in range(width):
        for j in range(height):
            cloth[x + i][y + j] += 1

for claim_id, x, y, width, height in claims:
    good = True
    for i in range(width):
        for j in range(height):
            if cloth[x + i][y + j] > 1:
                good = False

    if good:
        print(claim_id)
        break

