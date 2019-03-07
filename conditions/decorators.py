from functools import wraps
from inspect import signature
from typing import Union, List, Callable, Any

from conditions.exceptions import PreconditionViolatedError, PostconditionViolatedError


def precondition(parameter_selector: Union[int, str, List[Union[int, str]]], predicate: Callable[[Any], bool]) -> Any:
    """
    This is a factory that will create a decorator for a method based on a parameter selector and a predicate. The
    decorator will cause the method to raise an Exception (PreConditionViolatedError) if the selected parameter does not
    satisfy the predicate.
    :param parameter_selector: a selector that indicates which parameter(s) of the method should be checked. This may
    be an int for positional parameters or a string for keyword parameters. a list of any combination of ints and
    strings is also allowed; in that case, each of the selected parameters must match the predicate.
    :param predicate: a predicate that evaluates a parameter (single input function that returns True or False)
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

        @wraps(decorated_function)
        def condition(*args, **kwargs):
            """
            a decorated function that checks one or more parameter values of the original each match a given predicate.
            If the parameters do not match, the original function is never called.
            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameters matched the predicate
            :raises: PreConditionViolatedError if the parameters of the function do not match the predicate
            """
            bound = _signature.bind(*args, **kwargs)
            bound.apply_defaults()
            arguments = bound.arguments

            for parameter in parameter_selector:
                if isinstance(parameter, int):
                    key, value = list(arguments.items())[parameter]
                elif isinstance(parameter, str):
                    key, value = parameter, arguments[parameter]
                else:
                    raise Exception(f'Could not match parameter selector {parameter}')

                if not predicate(value):
                    raise PreconditionViolatedError.single_arg(key, value, predicate)

            return decorated_function(*args, **kwargs)
        return condition
    return decorator


def no_value_precondition(predicate: Callable[[], bool]) -> Any:
    def decorator(decorated_function):
        @wraps(decorated_function)
        def condition(*args, **kwargs):
            if not predicate():
                raise PreconditionViolatedError.no_arg(predicate)

            return decorated_function(*args, **kwargs)
        return condition
    return decorator


def multi_value_precondition(parameter_selector: List[Union[int, str]], predicate: Callable[..., bool]) -> Any:
    """
    This is a factory that will create a decorator for a method based on a parameter selector and a predicate. The
    decorator will cause the method to raise an Exception (PreConditionViolatedError) if the selected parameters do not
    satisfy the predicate.
    :param parameter_selector: a selector that indicates which parameters of the method should be checked. This may
    be ints for positional parameters or strings for keyword parameters. The parameter_selector will indicate some
    parameters, these will be passed (positionally in the listed order) to the predicate.
    :param predicate: a predicate that evaluates parameters (function that returns True or False)
    :return: a decorator based on the passed parameter selector and predicate
    """
    def decorator(decorated_function):
        """
        This decorator adds a check to this function that one of its parameters matches a predicate
        :param decorated_function: The function to be decorated
        :return: The decorated function
        """
        _signature = signature(decorated_function)

        @wraps(decorated_function)
        def condition(*args, **kwargs):
            """
            a decorated function that checks parameter values of the original match a given predicate.
            If the parameters do not match, the original function is never called.
            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameters matched the predicate
            :raises: PreConditionViolatedError if the parameters of the function do not match the predicate
            """
            bound = _signature.bind(*args, **kwargs)
            bound.apply_defaults()
            arguments = bound.arguments

            values = []
            key_value_pairs = []
            for parameter in parameter_selector:
                if isinstance(parameter, int):
                    key, value = list(arguments.items())[parameter]
                elif isinstance(parameter, str):
                    key, value = parameter, arguments[parameter]
                else:
                    raise Exception(f'Could not match parameter selector {parameter}')

                values.append(value)
                key_value_pairs.append((key, value))

            if not predicate(*values):
                raise PreconditionViolatedError.multi_arg(key_value_pairs, predicate)

            return decorated_function(*args, **kwargs)
        return condition
    return decorator


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
            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if it matches the predicate
            :raises: PostConditionViolatedError if the result of the function does not match the predicate
            """
            result = decorated_function(*args, **kwargs)
            if not predicate(result):
                raise PostconditionViolatedError(result, predicate)
            return result
        return condition
    return decorator
