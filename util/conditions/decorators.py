from collections import OrderedDict
from functools import wraps
from inspect import Signature, signature
from types import FunctionType
from typing import Any, Callable, List, Type, Union, cast

from util.conditions.exceptions import MalformedDecoratorError, PostconditionViolatedError, PreconditionViolatedError


def _verify_decorator_correctness(sig: Signature, parameter_selector: List[Union[int, str]],
                                  exception_factory: Union[Type[BaseException], Callable[..., BaseException]]) -> None:
    """
    Verifies that all selected parameters actually exist for a method.

    :param sig: A method signature
    :param parameter_selector: a selector that indicates parameter(s) of the method. This is a list with a combination
    of ints for positional parameters or strings for keyword parameters
    :raises MalformedDecoratorError: If one or more of the selected parameters does not exist in the method
    """
    for parameter in parameter_selector:
        if isinstance(parameter, int):
            if parameter < 0:
                raise MalformedDecoratorError(f'Positional parameter {parameter} out of range')
            try:
                sig.bind_partial(*([None] * (parameter + 1)))
            except TypeError:
                raise MalformedDecoratorError(f'Positional parameter {parameter} out of range')
        elif isinstance(parameter, str):
            try:
                sig.bind_partial(**{parameter: None})
            except TypeError:
                raise MalformedDecoratorError(f'Unknown keyword parameter {parameter}')
        else:
            raise MalformedDecoratorError(f'Parameter selector {parameter} has unknown type {type(parameter)}')

    if isinstance(exception_factory, type) and issubclass(exception_factory, BaseException):
        pass
    elif isinstance(exception_factory, FunctionType):
        pass
    else:
        raise MalformedDecoratorError(f'Incorrect type for exception_factory: {type(exception_factory)}')


def _get_bound_arguments(sig: Signature, *args, **kwargs) -> OrderedDict:
    """
    Bind the arguments based on a method signature

    :param sig: A method signature
    :param args: positional arguments
    :param kwargs: keyword arguments
    :return: An OrderedDict containing a mapping from variable names to the values they will have if the method is
    called with the passed arguments
    """
    bound = sig.bind(*args, **kwargs)
    bound.apply_defaults()
    return cast(OrderedDict, bound.arguments)


def _get_key_value_pairs(arguments: OrderedDict, parameter_selector: List[Union[int, str]]) -> OrderedDict:
    """
    Given all bound arguments for a function, return only those indicated by the argument selector

    :param arguments: An OrderedDict indicating all bound arguments for a function
    :param parameter_selector: a selector that indicates which parameters of the method should be checked. The list may
    contain ints for positional parameters or strings for keyword parameters.
    :return: An OrderedDict containing only those selected arguments (the order is determined by the parameter_selector)
    :raises MalformedDecoratorError: If one or more of the selected parameters does not exist in the method
    """
    result: OrderedDict = OrderedDict()

    argument_list = list(arguments.items())
    for parameter in parameter_selector:
        if isinstance(parameter, int):
            key, value = argument_list[parameter]
            result[key] = value
        elif isinstance(parameter, str):
            result[parameter] = arguments[parameter]
        else:
            raise MalformedDecoratorError(f'Could not match parameter selector {parameter}')

    return result


def _parameter_description(parameter_name: str, value: Any):
    return f"input parameter '{value}' of type {type(value)} (value for parameter {parameter_name})"


def precondition(parameter_selector: Union[int, str, List[Union[int, str]]], predicate: Callable[[Any], bool],
                 exception_factory: Union[Type[BaseException],
                                          Callable[[str], BaseException]]=PreconditionViolatedError) -> Any:
    """
    This is a factory that will create a decorator for a method based on a parameter selector and a predicate. The
    decorator will cause the method to raise an Exception (PreConditionViolatedError) if the selected parameter does not
    satisfy the predicate.

    :param parameter_selector: a selector that indicates which parameter(s) of the method should be checked. This may
    be an int for positional parameters or a string for keyword parameters. a list of any combination of ints and
    strings is also allowed; in that case, each of the selected parameters must match the predicate.
    :param predicate: a predicate that evaluates a parameter (single input function that returns True or False)
    :param exception_factory: Either an Exception class or a Callable that can create the desired Exception (defaults
    to PreconditionViolatedError)
    :return: a decorator based on the passed parameter selector and predicate
    """
    # Ensure we always have a list
    if not isinstance(parameter_selector, list):
        parameter_selector = [parameter_selector]

    def decorator(decorated_function):
        """
        This decorator adds a check to this function that one of its parameters matches a predicate

        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        _signature = signature(decorated_function)
        _verify_decorator_correctness(_signature, parameter_selector, exception_factory)

        @wraps(decorated_function)
        def function_with_condition(*args, **kwargs):
            """
            a decorated function that checks one or more parameter values of the original each match a given predicate.
            If the parameters do not match, the original function is never called.

            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameters matched the predicate
            :raises: PreConditionViolatedError if the parameters of the function do not match the predicate
            """
            arguments = _get_bound_arguments(_signature, *args, **kwargs)
            selected_parameters = _get_key_value_pairs(arguments, parameter_selector)

            for key, value in selected_parameters.items():
                if not predicate(value):
                    if isinstance(exception_factory, type) and issubclass(exception_factory, BaseException):
                        description = _parameter_description(key, value).capitalize()
                        message = f"{description} failed to pass precondition {predicate.__name__}"
                        raise exception_factory(message)
                    elif isinstance(exception_factory, FunctionType):
                        raise exception_factory(value)
                    else:
                        raise MalformedDecoratorError(
                            f'Incorrect type for exception_factory: {type(exception_factory)}')

            return decorated_function(*args, **kwargs)
        return function_with_condition

    return decorator


def no_value_precondition(predicate: Callable[[], bool],
                          exception_factory: Union[Type[BaseException],
                                                   Callable[[], BaseException]]=PreconditionViolatedError) -> Any:
    """
    This is a factory that will create a decorator for a method based on a predicate. The decorator will cause the
    method to raise an Exception (PreConditionViolatedError) if the predicate is not satisfied.

    :param predicate: a predicate (function that returns True or False)
    :param exception_factory: Either an Exception class or a Callable that can create the desired Exception (defaults
    to PreconditionViolatedError)
    :return: a decorator based on the passed predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that a predicate is satisfied

        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        _signature = signature(decorated_function)
        _verify_decorator_correctness(_signature, [], exception_factory)

        @wraps(decorated_function)
        def function_with_condition(*args, **kwargs):
            """
            a decorated function that checks whether a given predicate is satisfied.
            If the predicate is not satisfied, the original function is never called.

            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the predicate was satisfied
            :raises: PreConditionViolatedError if the predicate is not satisfied
            """
            if not predicate():
                if isinstance(exception_factory, type) and issubclass(exception_factory, BaseException):
                    message = f"Failed to pass precondition {predicate.__name__}"
                    raise exception_factory(message)
                elif isinstance(exception_factory, FunctionType):
                    raise exception_factory()
                else:
                    raise MalformedDecoratorError(f'Incorrect type for exception_factory: {type(exception_factory)}')


            return decorated_function(*args, **kwargs)
        return function_with_condition
    return decorator


def multi_value_precondition(parameter_selector: List[Union[int, str]], predicate: Callable[..., bool],
                             exception_factory: Union[Type[BaseException], Callable[[OrderedDict], BaseException]]
                             =PreconditionViolatedError) -> Any:
    """
    This is a factory that will create a decorator for a method based on a parameter selector and a predicate. The
    decorator will cause the method to raise an Exception (PreConditionViolatedError) if the selected parameters do not
    satisfy the predicate.

    :param parameter_selector: a selector that indicates which parameters of the method should be checked. This may
    be ints for positional parameters or strings for keyword parameters. The parameter_selector will indicate some
    parameters, these will be passed (positionally in the listed order) to the predicate.
    :param predicate: a predicate that evaluates parameters (function that returns True or False)
    :param exception_factory: Either an Exception class or a Callable that can create the desired Exception (defaults
    to PreconditionViolatedError)
    :return: a decorator based on the passed parameter selector and predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that one of its parameters matches a predicate

        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        _signature = signature(decorated_function)
        _verify_decorator_correctness(_signature, parameter_selector, exception_factory)

        @wraps(decorated_function)
        def function_with_condition(*args, **kwargs):
            """
            a decorated function that checks parameter values of the original match a given predicate.
            If the parameters do not match, the original function is never called.

            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameters matched the predicate
            :raises: PreConditionViolatedError if the parameters of the function do not match the predicate
            """
            arguments = _get_bound_arguments(_signature, *args, **kwargs)
            selected_parameters = _get_key_value_pairs(arguments, parameter_selector)

            if not predicate(*selected_parameters.values()):
                if isinstance(exception_factory, type) and issubclass(exception_factory, BaseException):
                    parameter_descriptions = map(lambda key_value: _parameter_description(*key_value),
                                                 selected_parameters.items())
                    descriptions = ', '.join(parameter_descriptions).capitalize()
                    message = f"{descriptions} failed to pass precondition {predicate.__name__}"
                    raise exception_factory(message)
                elif isinstance(exception_factory, FunctionType):
                    raise exception_factory(selected_parameters)
                else:
                    raise MalformedDecoratorError(f'Incorrect type for exception_factory: {type(exception_factory)}')

            return decorated_function(*args, **kwargs)
        return function_with_condition
    return decorator


def postcondition(predicate: Callable[[Any], bool],
                  exception_factory: Union[Type[BaseException],
                                           Callable[[Any], BaseException]]=PostconditionViolatedError) -> Any:
    """
    This is a factory that will create a decorator for a method based on a predicate. The decorator will cause the
    method to raise an Exception (PostConditionViolatedError) if the return value of the method does not satisfy the
    predicate.

    :param predicate: a predicate that evaluates a method's return value (single input function that returns True or
    False)
    :param exception_factory: Either an Exception class or a Callable that can create the desired Exception (defaults
    to PostconditionViolatedError)
    :return: a decorator based on the passed predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that upon its return the returned value matches a predicate.

        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        _signature = signature(decorated_function)
        _verify_decorator_correctness(_signature, [], exception_factory)

        @wraps(decorated_function)
        def function_with_condition(*args, **kwargs):
            """
            A decorated function that checks the returned value of the original matches a given predicate.

            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if it matches the predicate
            :raises: PostConditionViolatedError if the result of the function does not match the predicate
            """
            result = decorated_function(*args, **kwargs)
            if not predicate(result):
                if isinstance(exception_factory, type) and issubclass(exception_factory, BaseException):
                    message = f"Return value '{result}' of type {type(result)} failed to pass " \
                              f"postcondition {predicate.__name__}"
                    raise exception_factory(message)
                elif isinstance(exception_factory, FunctionType):
                    raise exception_factory(result)
                else:
                    raise MalformedDecoratorError(f'Incorrect type for exception_factory: {type(exception_factory)}')
            return result
        return function_with_condition
    return decorator
