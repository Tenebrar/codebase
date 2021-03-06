from typing import Callable, List

from hacker.hackvm.integers import verify_integer


class OperandStack:
    """
    Operand stack for the hack vm that allows the operations specified for that.
    Though it is called a stack, it allows for several non-stack operations (accessing elements other than the last
    pushed element).
    """

    def __init__(self) -> None:
        self._stack: List[int] = []  # Create an empty stack, as a list since we need access to all elements

    def push(self, value: int) -> None:
        """
        :param value: an integer
        :raises ValueError: if the input is outside the allowed integer range
        """
        verify_integer(value)
        self._stack.append(value)

    def pop(self) -> int:
        """
        Pops the last value from the stack
        :return: the popped value
        :raises RuntimeError: If the stack is empty
        """
        try:
            return self._stack.pop()
        except IndexError:
            raise RuntimeError('Stack underflow')

    def pick(self) -> None:
        """
        Push a copy of S<S0+1> (ex: 0^ duplicates S0)
        :raises RuntimeError: if there are not enough elements on the stack
        """
        index = self._pop_index()
        value = self._stack[index]
        self.push(value)

    def roll(self) -> None:
        """
        Remove S<S0+1> from the stack and push it on top (ex: 1v swaps S0 and S1)
        :raises RuntimeError: if there are not enough elements on the stack
        """
        index = self._pop_index()
        value = self._stack.pop(index)
        self.push(value)

    def _pop_index(self) -> int:
        """
        Pops an element from the stack to be used as an index, verifies that this index is inside the stack bounds
        :raises RuntimeError: If the popped index does not fit inside the stack
        :return: A negative value that can be used as an index in the stack (as a distance from the end)
        """
        index = self.pop()
        # These checks are necessary since python might interpret a negative value as a correct index
        if index < 0 or index >= len(self._stack):
            raise RuntimeError(f'Out of bounds. '
                               f'Accessing index {index} in stack {self._stack} (indices start at the end)')
        # Convert to index from end
        return -1 - index

    def add_two_operands(self) -> None:
        """
        Remove the first two elements from the stack and push their sum
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        self._perform_operator(lambda a, b: b + a)

    def subtract_two_operands(self) -> None:
        """
        Remove the first two elements from the stack and push their difference
        (The second element from the top is reduced by the first)
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        self._perform_operator(lambda a, b: b - a)

    def multiply_two_operands(self) -> None:
        """
        Remove the first two elements from the stack and push their product
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        self._perform_operator(lambda a, b: b * a)

    def divide_two_operands(self) -> None:
        """
        Remove the first two elements from the stack and push their division
        (The second element from the top is divided by the first)
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        # This is a change from the implementation at http://www.hacker.org/hvm/hackvm.py (we use integer division)
        self._perform_operator(lambda a, b: b // a)

    def cmp_two_operands(self) -> None:
        """
        Remove the first two elements from the stack and push their cmp
        (-1 if the second element from the top is smaller than the first, 0 if they are equal, or 1 otherwise)
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        # replacement for cmp suggested at: https://docs.python.org/3.0/whatsnew/3.0.html
        # int casts added because for some reason numpy complained about subtracting booleans
        self._perform_operator(lambda a, b: int(b > a) - int(b < a))

    def _perform_operator(self, operator: Callable[[int, int], int]) -> None:
        """
        Remove the first two elements from the stack and push the result of an operation on them
        (The operation is called with the first element on the stack first, and then the second)
        :param operator: A function mapping 2 operands to a result
        :raises RuntimeError: if there are less than 2 elements on the stack
        """
        value1 = self.pop()
        value2 = self.pop()
        result = operator(value1, value2)
        self.push(result)

    def __str__(self):
        return str(self._stack)

    def __len__(self):
        return len(self._stack)
