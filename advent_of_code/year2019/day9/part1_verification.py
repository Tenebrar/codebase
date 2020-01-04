from advent_of_code.util import input_file
from advent_of_code.year2019.day9.intcode import IntcodeComputer

with input_file() as file:
    PROGRAM = tuple(int(v) for v in file.readline().split(','))

computer = IntcodeComputer(list(PROGRAM))

computer.add_input(1)

computer.run()

print(computer.get_output())
