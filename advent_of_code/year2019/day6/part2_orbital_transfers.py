from collections import defaultdict
from typing import Dict, List

from advent_of_code.util import input_file


orbits = {}
with input_file() as file:
    for line in file:
        base, orbiter = line.strip().split(')')
        orbits[orbiter] = base

current = 'YOU'
you = []
while current != 'COM':
    you.append(current)
    current = orbits[current]

current = 'SAN'
san = []
while current != 'COM':
    san.append(current)
    current = orbits[current]

while you[-1] == san[-1]:
    you.pop(-1)
    san.pop(-1)

print(len(you) + len(san) - 2)
