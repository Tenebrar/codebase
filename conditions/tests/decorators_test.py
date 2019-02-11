from pytest import raises

from conditions.decorators import precondition, postcondition
from conditions.predicates import is_strict_positive, is_not_none
from conditions.exceptions import PostConditionViolatedError, PreConditionViolatedError


def test_function_success():
    @precondition('num', is_strict_positive)
    @postcondition(is_strict_positive)
    def fun(num: int) -> int:
        return num

    fun(3)  # Runs without Exception


def test_function_precondition_by_name_param_by_name_failure():
    @precondition('num', is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PreConditionViolatedError):
        fun(num=-3)


def test_function_precondition_by_name_param_by_pos_failure():
    @precondition('num', is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PreConditionViolatedError):
        fun(-3)


def test_function_precondition_by_pos_param_by_name_failure():
    @precondition(0, is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PreConditionViolatedError):
        fun(num=-3)


def test_function_precondition_by_pos_param_by_pos_failure():
    @precondition(0, is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PreConditionViolatedError):
        fun(-3)


def test_function_postcondition_failure():
    @postcondition(is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PostConditionViolatedError):
        fun(-3)


def test_multiple_params_same_condition():
    @precondition([0, 1], is_strict_positive)
    def fun(num: int, ber: int) -> int:
        return num + ber

    with raises(PreConditionViolatedError):
        fun(-3, 3)
    with raises(PreConditionViolatedError):
        fun(3, -3)
