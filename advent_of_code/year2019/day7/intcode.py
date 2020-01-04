from abc import ABC, abstractmethod
from typing import List, Dict, Callable


class Operation(ABC):
    @abstractmethod
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        ...


class ReadReadWriteOperation(Operation, ABC):
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        parameter1 = computer._get_parameter(parameter_modes, 1)
        parameter2 = computer._get_parameter(parameter_modes, 2)

        computer._set_parameter(3, self.get_value(parameter1, parameter2))

        computer.index += 4

    @abstractmethod
    def get_value(self, parameter1: int, parameter2: int):
        ...


class AddOperation(ReadReadWriteOperation):
    def get_value(self, parameter1: int, parameter2: int):
        return parameter1 + parameter2


class MultiplyOperation(ReadReadWriteOperation):
    def get_value(self, parameter1: int, parameter2: int):
        return parameter1 * parameter2


class InputOperation(Operation):
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        if not computer.inputs:
            raise StopIteration()  # Stop execution until input is added
        computer._set_parameter(1, computer.inputs.pop(0))

        computer.index += 2


class OutputOperation(Operation):
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        parameter1 = computer._get_parameter(parameter_modes, 1)

        computer.outputs.append(parameter1)

        computer.index += 2


class ConditionalJumpOperation(Operation, ABC):
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        parameter1 = computer._get_parameter(parameter_modes, 1)
        parameter2 = computer._get_parameter(parameter_modes, 2)

        if self.condition(parameter1):
            computer.index = parameter2
        else:
            computer.index += 3

    @abstractmethod
    def condition(self, parameter1: int) -> bool:
        ...


class JumpIfNonZeroOperation(ConditionalJumpOperation):
    def condition(self, parameter1: int) -> bool:
        return parameter1 != 0


class JumpIfZeroOperation(ConditionalJumpOperation):
    def condition(self, parameter1: int) -> bool:
        return parameter1 == 0


class LessThanOperation(ReadReadWriteOperation):
    def get_value(self, parameter1: int, parameter2: int):
        return 1 if parameter1 < parameter2 else 0


class EqualsOperation(ReadReadWriteOperation):
    def get_value(self, parameter1: int, parameter2: int):
        return 1 if parameter1 == parameter2 else 0


class StopOperation(Operation):
    def execute(self, computer: 'IntcodeComputer', parameter_modes: str):
        computer.done = True
        raise StopIteration()


class IntcodeComputer:
    @classmethod
    def from_string(cls, program: str):
        return IntcodeComputer([int(value) for value in program.split(',')])

    def __init__(self, program: List[int]):
        self.program: List[int] = program
        self.inputs: List[int] = []
        self.outputs: List[int] = []
        self.index: int = 0
        self.done = False

        self.parameter_modes: Dict[str, Callable[[int], int]] = {
            '0': lambda value: self.program[value],
            '1': lambda value: value
        }

        self.operations: Dict[int, Operation] = {
            1: AddOperation(),
            2: MultiplyOperation(),
            3: InputOperation(),
            4: OutputOperation(),
            5: JumpIfNonZeroOperation(),
            6: JumpIfZeroOperation(),
            7: LessThanOperation(),
            8: EqualsOperation(),
            99: StopOperation()
        }

    def add_input(self, value: int) -> None:
        self.inputs.append(value)

    def get_output(self) -> int:
        return self.outputs.pop(0)

    def _get_parameter(self, parameter_modes, parameter_number):
        value = self.program[self.index + parameter_number]
        return self.parameter_modes[parameter_modes[parameter_number - 1]](value)

    def _set_parameter(self, parameter_number, value):
        self.program[self.program[self.index + parameter_number]] = value

    def run(self):
        try:
            while True:
                op_code = self.program[self.index] % 100
                parameter_modes = f'000{self.program[self.index] // 100}'[::-1]  # Zero-padded for convenience

                self.operations[op_code].execute(self, parameter_modes)
        except StopIteration:
            pass
