from functools import partial
from logging import getLogger, StreamHandler
from numpy import zeros
from typing import List, Sequence

from hacker.hackvm.counter import IterationCounter
from hacker.hackvm.operand_stack import OperandStack
from hacker.hackvm.stack import Stack

logger = getLogger(__name__)
logger.addHandler(StreamHandler())

DEFAULT_MAX_ITERATIONS = 10000
MEMORY_SIZE = 16384


# Adapted from http://www.hacker.org/hvm/hackvm.py, with explanations on http://www.hacker.org/hvm/
class HackVm:
    """ VM that runs programs in the hackvm language """
    def __init__(self, max_iterations=DEFAULT_MAX_ITERATIONS) -> None:
        """
        Initializes the vm
        :param max_iterations: The default maximum iterations is 10k, but some challenges set it to something else
        """
        self._memory = zeros(MEMORY_SIZE, dtype=int)
        self._call_stack = Stack()
        self._operand_stack = OperandStack()
        self._program_counter = 0

        self._iteration_counter = IterationCounter(max_iterations)

        # These are instance variables because they need to be accessible to the operations
        self._program = None  # Will be set in the run method
        self._result: List[str] = []

        self._operations = {
            ' ': lambda: None,  # NO_OP
            '\n': lambda: None,  # NO_OP
            'p': self._print_int,
            'P': self._print_char,
            '0': partial(self._operand_stack.push, 0),
            '1': partial(self._operand_stack.push, 1),
            '2': partial(self._operand_stack.push, 2),
            '3': partial(self._operand_stack.push, 3),
            '4': partial(self._operand_stack.push, 4),
            '5': partial(self._operand_stack.push, 5),
            '6': partial(self._operand_stack.push, 6),
            '7': partial(self._operand_stack.push, 7),
            '8': partial(self._operand_stack.push, 8),
            '9': partial(self._operand_stack.push, 9),
            '+': self._operand_stack.add_two_operands,
            '-': self._operand_stack.subtract_two_operands,
            '*': self._operand_stack.multiply_two_operands,
            '/': self._operand_stack.divide_two_operands,
            ':': self._operand_stack.cmp_two_operands,
            'g': self._jump,
            '?': self._jump_if_zero,
            'c': self._call,
            '$': self._return,
            '<': self._read_from_memory,
            '>': self._write_to_memory,
            '^': self._operand_stack.pick,
            'v': self._operand_stack.roll,
            'd': self._operand_stack.pop,
            '!': self._end,
        }

    def run(self, program: str, initial_memory: Sequence[int]=(), verbose: bool=False) -> str:
        """
        Runs a hackvm program
        :param program: A hackvm program
        :param initial_memory: Values for the initial memory of the program (Needs only to indicate non-0 values)
        :param verbose: Whether to output each execute operation and resulting stack
        :return: The output of the program
        :raises RuntimeError: If the program counter goes out of bounds of the program, or the maximum iteration
        count is exceeded
        """
        self._program = program
        self._memory[:len(initial_memory)] = initial_memory
        logger.setLevel('DEBUG' if verbose else 'WARNING')

        while self._program_counter != len(self._program):
            op_code = self._program[self._program_counter]
            logger.debug(f'@{self._program_counter} {op_code}')
            self._program_counter += 1

            self._operations[op_code]()
            logger.debug(self._operand_stack)

            self._verify_validity()

        return ''.join(self._result)

    def _verify_validity(self):
        """ Verify the iteration count has not been exceeded and the program counter is in bounds """
        self._iteration_counter.increment()
        if not 0 <= self._program_counter <= len(self._program):
            raise RuntimeError(f'Out of code bounds, {self._program_counter}')

    def _print_char(self) -> None:
        value = self._operand_stack.pop()
        self._result.append(chr(value & 0x7F))

    def _print_int(self) -> None:
        value = self._operand_stack.pop()
        self._result.append(str(value))

    def _jump(self) -> None:
        self._program_counter += self._operand_stack.pop()

    def _jump_if_zero(self) -> None:
        offset = self._operand_stack.pop()
        if self._operand_stack.pop() == 0:
            self._program_counter += offset

    def _call(self) -> None:
        self._call_stack.push(self._program_counter)
        self._program_counter = self._operand_stack.pop()

    def _return(self) -> None:
        self._program_counter = self._call_stack.pop()

    def _read_from_memory(self) -> None:
        memory_address = self._validate_memory_address(self._operand_stack.pop())
        self._operand_stack.push(self._memory[memory_address])

    def _write_to_memory(self) -> None:
        memory_address = self._validate_memory_address(self._operand_stack.pop())
        self._memory[memory_address] = self._operand_stack.pop()

    def _validate_memory_address(self, memory_address: int) -> int:
        if memory_address < 0 or memory_address >= len(self._memory):
            raise RuntimeError(f'Invalid memory access, index {memory_address}')
        return memory_address

    def _end(self) -> None:
        self._program_counter = len(self._program)
