from pytest import raises

from conditions.decorators import multi_value_precondition, no_value_precondition, postcondition, precondition
from conditions.exceptions import MalformedDecoratorError, PostconditionViolatedError, PreconditionViolatedError
from conditions.predicates import is_strict_positive


def test_function_success() -> None:
    @precondition('num', is_strict_positive)
    @no_value_precondition(lambda: True)
    @multi_value_precondition(['num', 1], lambda s, t: True)
    @postcondition(is_strict_positive)
    def fun(num: int, num2: int) -> int:
        return num + num2

    fun(3, 2)  # Runs without Exception


def test_function_precondition_by_name_param_by_name_failure() -> None:
    @precondition('num', is_strict_positive)  # select the parameter by name
    def fun(num: int) -> int:
        return num

    with raises(PreconditionViolatedError):
        fun(num=-3)  # call the function by name


def test_function_precondition_by_name_param_by_pos_failure() -> None:
    @precondition('num', is_strict_positive)  # select the parameter by name
    def fun(num: int) -> int:
        return num

    with raises(PreconditionViolatedError):
        fun(-3)  # call the function by position


def test_function_precondition_by_pos_param_by_name_failure() -> None:
    @precondition(0, is_strict_positive)  # select the parameter by position
    def fun(num: int) -> int:
        return num

    with raises(PreconditionViolatedError):
        fun(num=-3)  # call the function by name


def test_function_precondition_by_pos_param_by_pos_failure() -> None:
    @precondition(0, is_strict_positive)  # select the parameter by position
    def fun(num: int) -> int:
        return num

    with raises(PreconditionViolatedError):
        fun(-3)  # call the function by position


def test_function_postcondition_failure() -> None:
    @postcondition(is_strict_positive)
    def fun(num: int) -> int:
        return num

    with raises(PostconditionViolatedError):
        fun(-3)


def test_multiple_params_same_condition() -> None:
    @precondition([0, 1], is_strict_positive)
    def fun(num: int, ber: int) -> int:
        return num + ber

    with raises(PreconditionViolatedError):
        fun(-3, 3)
    with raises(PreconditionViolatedError):
        fun(3, -3)


def test_no_value_precondition() -> None:
    @no_value_precondition(lambda: False)
    def fun(num: int) -> int:
        return num

    with raises(PreconditionViolatedError):
        fun(3)


def test_multi_value_precondition() -> None:
    def is_greater_than(a: int, b: int) -> bool:
        return a > b

    @multi_value_precondition([0, 1], is_greater_than)
    def fun(c: int, d: int) -> int:
        return c - d

    assert fun(5, 3) == 2
    with raises(PreconditionViolatedError):
        fun(3, 5)


def test_function_precondition_by_name_incorrect_name() -> None:
    with raises(MalformedDecoratorError):
        @precondition('wrong', is_strict_positive)
        def fun(num: int) -> int:
            return num


def test_function_precondition_by_pos_incorrect_pos() -> None:
    with raises(MalformedDecoratorError):
        @precondition(1, is_strict_positive)
        def fun(num: int) -> int:
            return num


def test_function_precondition_by_pos_negative_pos() -> None:
    with raises(MalformedDecoratorError):
        @precondition(-1, is_strict_positive)
        def fun(num: int) -> int:
            return num
