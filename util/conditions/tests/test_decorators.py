from pytest import raises

from util.conditions.decorators import multi_value_precondition, no_value_precondition, postcondition, precondition
from util.conditions.exceptions import MalformedDecoratorError, PostconditionViolatedError, PreconditionViolatedError
from util.conditions.predicates import is_strict_positive


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


def test_function_precondition_exception_factory_type() -> None:
    @precondition('num', is_strict_positive, ValueError)
    def fun(num: int) -> int:
        return num

    with raises(ValueError):
        fun(num=-3)


def test_function_precondition_exception_factory_lambda() -> None:
    @precondition('num', is_strict_positive, lambda v: ValueError())
    def fun(num: int) -> int:
        return num

    with raises(ValueError):
        fun(num=-3)


def test_function_precondition_exception_factory_incorrect_type() -> None:
    with raises(MalformedDecoratorError):
        @precondition('num', is_strict_positive, str)
        def fun(num: int) -> int:
            return num


def test_function_no_value_precondition_exception_factory_type() -> None:
    @no_value_precondition(lambda: False, ValueError)
    def fun(num: int) -> int:
        return num

    with raises(ValueError):
        fun(num=-3)


def test_function_no_value_precondition_exception_factory_lambda() -> None:
    @no_value_precondition(lambda: False, lambda: ValueError())
    def fun(num: int) -> int:
        return num

    with raises(ValueError):
        fun(num=-3)


def test_function_no_value_precondition_exception_factory_incorrect_type() -> None:
    with raises(MalformedDecoratorError):
        @no_value_precondition(lambda: False, str)
        def fun(num: int) -> int:
            return num


def test_function_multi_value_precondition_exception_factory_type() -> None:
    def is_greater_than(a: int, b: int) -> bool:
        return a > b

    @multi_value_precondition([0, 1], is_greater_than, ValueError)
    def fun(c: int, d: int) -> int:
        return c - d

    assert fun(5, 3) == 2
    with raises(ValueError):
        fun(3, 5)


def test_function_multi_value_precondition_exception_factory_lambda() -> None:
    def is_greater_than(a: int, b: int) -> bool:
        return a > b

    @multi_value_precondition([0, 1], is_greater_than, lambda d: ValueError())
    def fun(c: int, d: int) -> int:
        return c - d

    assert fun(5, 3) == 2
    with raises(ValueError):
        fun(3, 5)


def test_function_multi_value_precondition_exception_factory_incorrect_type() -> None:
    def is_greater_than(a: int, b: int) -> bool:
        return a > b

    with raises(MalformedDecoratorError):
        @multi_value_precondition([0, 1], is_greater_than, str)
        def fun(c: int, d: int) -> int:
            return c - d
