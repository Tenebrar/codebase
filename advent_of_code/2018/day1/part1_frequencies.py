from advent_of_code.util import input_file

with input_file() as file:
    print(sum(int(line) for line in file))
