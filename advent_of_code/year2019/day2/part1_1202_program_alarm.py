from typing import List

from advent_of_code.util import input_file


def intcode(program: List[int]) -> None:
    index = 0

    while True:
        op_code = program[index]

        if op_code == 1:
            program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
        elif op_code == 2:
            program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]
        elif op_code == 99:
            break
        else:
            raise Exception()

        index += 4


with input_file() as file:
    program = [int(v) for v in file.readline().split(',')]


program[1] = 12
program[2] = 2

intcode(program)

print(program[0])
