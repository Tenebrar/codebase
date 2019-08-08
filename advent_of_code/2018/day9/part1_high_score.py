from collections import defaultdict
from re import search

from advent_of_code.util import input_file

with input_file() as file:
    match = search('^(\d+) players; last marble is worth (\d+) points\n$', file.read())
    players, points = int(match.group(1)), int(match.group(2))

circle = [0]
current_value = 1
current_index = 0
current_player = 1
score = defaultdict(int)

for _ in range(points):
    if current_value % 23 != 0:
        current_index = (current_index + 2) % len(circle)
        circle.insert(current_index, current_value)
    else:
        current_index = (current_index - 7) % len(circle)
        marble_score = current_value + circle.pop(current_index)
        score[current_player] += marble_score

    current_value += 1
    current_player = current_player % players + 1

print(max(score.values()))
