from functools import wraps
from inspect import signature
from typing import Any

from conditions.exceptions import IncorrectConditionFormatError, PreConditionViolatedError, PostConditionViolatedError
from conditions.predicates import is_not_none, is_strict_positive


def precondition(parameter_selector, predicate):
    """
    This is a factory that will create a decorator for a method based on a parameter selection and a predicate. The
    decorator will cause the method to raise an Exception (PreConditionViolatedError) if the selected parameter does not
    satisfy the predicate.
    :param parameter_selector: a selector that indicates which parameter(s) of the method should be checked. This may
    be an int for positional parameters or a string for keyword parameters. a list of any combination of ints and
    strings is also allowed; in that case, each of the selected parameters must match the predicate.
    :param predicate: a predicate that evaluates a parameter (single input function that returns True or False)
    :return: a decorator based on the passed parameter selector and predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that one of its parameters matches a predicate
        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        parameters = signature(decorated_function).parameters
        if isinstance(parameter_selector, list):
            parameter_names = [_normalize(selector, parameters) for selector in parameter_selector]
        else:
            parameter_names = [_normalize(parameter_selector, parameters)]

        @wraps(decorated_function)
        def condition(*args, **kwargs):
            """
            a decorated function that checks a parameter value of the original matches a given predicate.
            If the parameter does not match, the original function is never called.
            :param args: The regular arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameter matched the predicate
            :raises: PreConditionViolatedError if the parameter of the function does not match the predicate
            """
            for index in range(len(args)):
                kwargs[list(parameters.items())[index][0]] = args[index]
            args = []  # To avoid multiple values for argument in decorated function

            for parameter_name in parameter_names:
                try:
                    value = kwargs[parameter_name]
                except KeyError:
                    value = parameters[parameter_name].default

                if not predicate(value):
                    raise PreConditionViolatedError(f'{value} (value of parameter {parameter_name})'
                                                    f' failed to pass precondition {predicate.__name__}')
            return decorated_function(*args, **kwargs)
        return condition
    return decorator


def _normalize(parameter_selector, parameters):
    """
    Convert a single parameter selector into a parameter name
    :param parameter_selector: An int or string indicating a parameter
    :param parameters: The function's parameters
    :return: The parameter name corresponding to the selector
    :rtype: str
    """
    if isinstance(parameter_selector, int):
        index = parameter_selector
        if index < 0 or index >= len(parameters):
            raise IncorrectConditionFormatError(
                f'Index {index} on a function with {len(parameters)} parameters')
        name = list(parameters.items())[index][0]
    elif isinstance(parameter_selector, str):
        name = parameter_selector
        if name not in parameters:
            raise IncorrectConditionFormatError(
                f"Name '{name}' on a function with only parameters: {parameters.keys()}")
    else:
        raise ValueError(f'Parameter of type {type(parameter_selector)} not allowed for parameter selection')
    return name


def postcondition(predicate):
    """
    This is a factory that will create a decorator for a method based on a predicate. The decorator will cause the
    method to raise an Exception (PostConditionViolatedError) if the return value of the method does not satisfy the
    predicate
    :param predicate: a predicate that evaluates a method's return value (single input function that returns True or
    False)
    :return: a decorator based on the passed predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that upon its return the returned value matches a predicate
        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        @wraps(decorated_function)
        def condition(*args, **kwargs):
            """
            a decorated function that checks the returned value of the original matches a given predicate
            :param args: The regular arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if it matches the predicate
            :raises: PostConditionViolatedError if the result of the function does not match the predicate
            """
            result = decorated_function(*args, **kwargs)
            if not predicate(result):
                raise PostConditionViolatedError(
                    f"Return value '{result}' of type {type(result)} failed to pass postcondition {predicate.__name__}")
            return result
        return condition
    return decorator


# TODO if this works with precondition, move it to predicates
def is_greater_than(a, b):
    print(f'checking {a} and {b}')
    return a > b


# TODO replace with tests
@precondition(0, is_strict_positive)
@precondition('num', is_strict_positive)
@precondition(['num', 0], is_strict_positive)
@precondition(1, is_not_none)
# @precondition((0, 1), is_greater_than)  # TODO
@postcondition(is_strict_positive)
def example(num: int, obj: Any=[]) -> int:
    if obj is None:
        raise ZeroDivisionError('Simulates something going wrong when the argument is wrong')
    return num - 2


res = example(3)
print(f'result = {res}')
try:
    example(2)
except PostConditionViolatedError:
    print('Postcondition failed as expected')
try:
    example(0)
except PreConditionViolatedError:
    print('Precondition failed as expected')
try:
    example(3, None)
except PreConditionViolatedError:
    print('Precondition failed as expected')

