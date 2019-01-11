from pytest import fixture, mark, param, raises
from typing import List

from hacker.hackvm.operand_stack import OperandStack


@fixture
def stack():
    return OperandStack()


def to_list(stack: OperandStack) -> List[int]:
    # Used here to be able to replace should implementation change, but this really helps testing
    return stack._stack


def make(stack: OperandStack, values: List[int]) -> None:
    assert len(stack) == 0
    for value in values:
        stack.push(value)
    assert to_list(stack) == values


def test_stack_push_and_pop(stack: OperandStack) -> None:
    assert to_list(stack) == []
    stack.push(4)
    assert to_list(stack) == [4]
    stack.push(5)
    assert to_list(stack) == [4, 5]
    stack.push(6)
    assert to_list(stack) == [4, 5, 6]

    assert stack.pop() == 6
    assert to_list(stack) == [4, 5]
    assert stack.pop() == 5
    assert to_list(stack) == [4]
    assert stack.pop() == 4
    assert to_list(stack) == []


@mark.parametrize('values,expected', (
    param([4, 5, 6, 0], [4, 5, 6, 6]),
    param([4, 5, 6, 1], [4, 5, 6, 5]),
    param([4, 5, 6, 2], [4, 5, 6, 4]),
))
def test_pick(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.pick()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([4, 5, 6, 3]),  # Out of bounds
    param([4, 5, 6, -1]),  # Out of bounds
    param([]),  # No index to pop
    param([0]),  # Out of bounds (no values but index)
))
def test_pick_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.pick()


@mark.parametrize('values,expected', (
    param([4, 5, 6, 0], [4, 5, 6]),
    param([4, 5, 6, 1], [4, 6, 5]),
    param([4, 5, 6, 2], [5, 6, 4]),
))
def test_roll(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.roll()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([4, 5, 6, 3]),  # Out of bounds
    param([4, 5, 6, -1]),  # Out of bounds
    param([]),  # No index to pop
    param([0]),  # Out of bounds (no values but index)
))
def test_roll_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.roll()


@mark.parametrize('values,expected', (
    param([4, 5, 6], [4, 11]),
    param([4, 5], [9]),
    param([0, 0], [0]),
    param([-2, -3], [-5]),
))
def test_add_two_operands(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.add_two_operands()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([]),
    param([4]),
))
def test_add_two_operands_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.add_two_operands()


@mark.parametrize('values,expected', (
    param([4, 5, 6], [4, -1]),
    param([4, 5], [-1]),
    param([0, 0], [0]),
    param([-2, -3], [1]),
))
def test_subtract_two_operands(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.subtract_two_operands()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([]),
    param([4]),
))
def test_subtract_two_operands_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.subtract_two_operands()


@mark.parametrize('values,expected', (
    param([4, 5, 6], [4, 30]),
    param([4, 5], [20]),
    param([0, 0], [0]),
    param([-2, -3], [6]),
))
def test_multiply_two_operands(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.multiply_two_operands()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([]),
    param([4]),
))
def test_multiply_two_operands_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.multiply_two_operands()


@mark.parametrize('values,expected', (
    param([4, 5, 6], [4, 0]),
    param([5, 4], [1]),
    param([0, 1], [0]),
    param([-2, -3], [0]),
    param([15, -3], [-5]),
))
def test_divide_two_operands(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.divide_two_operands()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([]),
    param([4]),
))
def test_divide_two_operands_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.divide_two_operands()


def test_divide_two_operands_by_zero(stack: OperandStack) -> None:
    make(stack, [4, 0])
    with raises(ZeroDivisionError):
        stack.divide_two_operands()


@mark.parametrize('values,expected', (
    param([4, 5, 6], [4, -1]),
    param([5, 4], [1]),
    param([0, 0], [0]),
    param([-2, -3], [1]),
))
def test_cmp_two_operands(stack: OperandStack, values: List[int], expected: List[int]) -> None:
    make(stack, values)
    stack.cmp_two_operands()
    assert to_list(stack) == expected


@mark.parametrize('values', (
    param([]),
    param([4]),
))
def test_cmp_two_operands_fail(stack: OperandStack, values: List[int]) -> None:
    make(stack, values)
    with raises(RuntimeError):
        stack.cmp_two_operands()