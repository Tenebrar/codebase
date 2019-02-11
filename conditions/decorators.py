from functools import wraps
from inspect import signature
from typing import Union, List, Callable, Any

from conditions.exceptions import PreConditionViolatedError, PostConditionViolatedError


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
            a decorated function that checks a parameter value of the original matches a given predicate.
            If the parameter does not match, the original function is never called.
            :param args: The positional arguments for the original function
            :param kwargs: The keyword arguments for the original function
            :return: The result of the function if the parameter matched the predicate
            :raises: PreConditionViolatedError if the parameter of the function does not match the predicate
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
                    raise PreConditionViolatedError(key, value, predicate)

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
                raise PostConditionViolatedError(result, predicate)
            return result
        return condition
    return decorator
