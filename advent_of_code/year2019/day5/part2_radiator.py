from typing import List

from advent_of_code.util import input_file


def intcode(program: List[int]) -> None:
    index = 0

    while True:
        op_code = program[index] % 100
        parameter_modes = f'000{program[index] // 100}'

        if op_code == 1:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            program[program[index + 3]] = parameter1 + parameter2
            index += 4
        elif op_code == 2:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            program[program[index + 3]] = parameter1 * parameter2
            index += 4
        elif op_code == 3:
            program[program[index + 1]] = 5  # Input is 5 for this exercise
            index += 2
        elif op_code == 4:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]

            print(parameter1)
            index += 2
        elif op_code == 5:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            if parameter1:
                index = parameter2
            else:
                index += 3
        elif op_code == 6:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            if not parameter1:
                index = parameter2
            else:
                index += 3
        elif op_code == 7:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            program[program[index + 3]] = 1 if parameter1 < parameter2 else 0

            index += 4
        elif op_code == 8:
            parameter1 = program[program[index + 1]] if parameter_modes[-1] == '0' else program[index + 1]
            parameter2 = program[program[index + 2]] if parameter_modes[-2] == '0' else program[index + 2]

            program[program[index + 3]] = 1 if parameter1 == parameter2 else 0

            index += 4
        elif op_code == 99:
            break
        else:
            raise Exception()


with input_file() as file:
    program = [int(v) for v in file.readline().split(',')]

intcode(program)
