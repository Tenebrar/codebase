from typing import List

from advent_of_code.util import input_file


DESIRED_RESULT = 19690720


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


for noun in range(0, 100):
    for verb in range(0, 100):
        with input_file() as file:
            program = [int(v) for v in file.readline().split(',')]

        program[1] = noun
        program[2] = verb

        intcode(program)

        output = program[0]

        if output == DESIRED_RESULT:
            print(noun * 100 + verb)
