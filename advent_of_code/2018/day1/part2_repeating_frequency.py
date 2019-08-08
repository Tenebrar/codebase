from itertools import cycle

from advent_of_code.util import input_file

with input_file() as file:
    frequency_changes = [int(line) for line in file]

frequency = 0
known_frequencies = {0}
for frequency_change in cycle(frequency_changes):
    frequency = frequency + frequency_change
    if frequency in known_frequencies:
        break
    known_frequencies.add(frequency)

print(frequency)
