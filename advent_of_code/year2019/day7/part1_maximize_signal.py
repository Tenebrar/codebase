from itertools import permutations

from advent_of_code.util import input_file
from advent_of_code.year2019.day7.intcode import IntcodeComputer

with input_file() as file:
    PROGRAM = tuple(int(v) for v in file.readline().split(','))


max_output = 0
for permutation in permutations([0,1,2,3,4]):
    output = 0
    for phase in permutation:
        computer = IntcodeComputer(list(PROGRAM))
        computer.add_input(phase)
        computer.add_input(output)

        computer.run()
        output = computer.get_output()

    max_output = max(max_output, output)

print(max_output)
