from typing import List


class Stack:
    """ Implementation of a stack, with only its 2 most basic functions """

    def __init__(self) -> None:
        self._stack: List[int] = []

    def push(self, value: int) -> None:
        """ Push a value onto the stack """
        self._stack.append(value)

    def pop(self) -> int:
        """ Pop a value from the stack """
        return self._stack.pop()