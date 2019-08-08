from typing import Set

from advent_of_code.util import input_file

with input_file() as file:
    labels = [line.rstrip('\n') for line in file]


def get_repeat_counts(label: str) -> Set[int]:
    label = sorted(label)

    letter = label.pop()
    count = 1
    counts = set()

    while label:
        new_letter = label.pop()
        if letter == new_letter:
            count += 1
        else:
            counts.add(count)
            count = 1
        letter = new_letter
    counts.add(count)
    return counts


two_repeating = 0
three_repeating = 0
for label in labels:
    counts = get_repeat_counts(label)

    if 2 in counts:
        two_repeating += 1
    if 3 in counts:
        three_repeating += 1

print(f'Labels with letter repeating exactly twice: {two_repeating}')
print(f'Labels with letter repeating exactly three times: {three_repeating}')
print(f'Product: {two_repeating * three_repeating}')

