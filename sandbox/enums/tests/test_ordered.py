from enum import auto, unique
from mock import patch, Mock, call
from pytest import raises

from sandbox.enums.ordered import OrderedEnum, comparison_method


def test_ordering():
    """ Tests that the ordering is as expected (based on the order, not the values) """
    @unique
    class TestEnum(OrderedEnum):
        FIRST = 2
        SECOND = 1

    assert not TestEnum.FIRST < TestEnum.FIRST
    assert TestEnum.FIRST <= TestEnum.FIRST
    assert TestEnum.FIRST == TestEnum.FIRST
    assert TestEnum.FIRST >= TestEnum.FIRST
    assert not TestEnum.FIRST > TestEnum.FIRST

    assert TestEnum.FIRST < TestEnum.SECOND
    assert TestEnum.FIRST <= TestEnum.SECOND
    assert not TestEnum.FIRST == TestEnum.SECOND
    assert not TestEnum.FIRST >= TestEnum.SECOND
    assert not TestEnum.FIRST > TestEnum.SECOND

    assert not TestEnum.SECOND < TestEnum.FIRST
    assert not TestEnum.SECOND <= TestEnum.FIRST
    assert not TestEnum.SECOND == TestEnum.FIRST
    assert TestEnum.SECOND >= TestEnum.FIRST
    assert TestEnum.SECOND > TestEnum.FIRST


def test_not_comparable_to_other_classes():
    """
    Tests that comparison fails when comparing to other classes (equality returning False, the others raising TypeError)
    """
    @unique
    class TestEnum1(OrderedEnum):
        FIRST = auto()

    @unique
    class TestEnum2(OrderedEnum):
        SECOND = auto()

    with raises(TypeError):
        TestEnum1.FIRST < TestEnum2.SECOND
    with raises(TypeError):
        TestEnum1.FIRST <= TestEnum2.SECOND
    with raises(TypeError):
        TestEnum1.FIRST > TestEnum2.SECOND
    with raises(TypeError):
        TestEnum1.FIRST >= TestEnum2.SECOND
    assert TestEnum1.FIRST != TestEnum2.SECOND


def test_comparison_method_decorator_different_type():
    """
    Tests that the comparison_method decorator causes the function to return NotImplemented if the types do not match,
    without ever calling the decorated function
    """
    mock = Mock()

    @comparison_method
    def test_function(*args, **kwargs):
        mock(args, kwargs)
        return None

    assert test_function('test', 0) == NotImplemented
    assert not mock.called


def test_comparison_method_decorator_same_type():
    """
    Tests that the comparison_method decorator calls the decorated function with the arguments unchanged if the types
    match
    """
    mock = Mock()

    @comparison_method
    def test_function(*args, **kwargs):
        mock(args, kwargs)
        return None

    assert test_function('test', 'test2') is None
    assert mock.call_count == 1
    assert mock.call_args_list[0] == call(('test', 'test2'), {})
