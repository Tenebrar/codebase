from pytest import raises

from hacker.hackvm.stack import Stack


def test_stack():
    stack = Stack()

    stack.push(3)
    stack.push(4)
    assert stack.pop() == 4
    stack.push(5)
    assert stack.pop() == 5
    assert stack.pop() == 3

    with raises(Exception):
        stack.pop()