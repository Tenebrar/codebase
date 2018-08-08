from functools import wraps
import inspect
from sandbox.conditions.predicates import is_not_none


def precondition(parameter_description, predicate):
    def decorator(original_function):
        @wraps(original_function)
        def wrapped_function(*args, **kwargs):
            for param in _get_parameters(parameter_description, original_function, *args, **kwargs):
                if not predicate(param):
                    raise Exception(f'Precondition {predicate} not met by {param}')

            return original_function(*args, **kwargs)
        return wrapped_function
    return decorator


def _get_parameters(parameter_description, original_function, *args, **kwargs):
    print('arguments')
    print(args)
    print(kwargs)

    signature = inspect.signature(original_function).parameters

    # TODO normalize arguments into a single dict {parameter name: value}
    arguments = dict(kwargs)

    # Normalize parameter_description to a list of strings (parameter names)
    if not isinstance(parameter_description, list):
        parameter_description = [parameter_description]
    parameter_description = [param if isinstance(param, str) else list(signature.keys())[param]
                             for param in parameter_description]
    for param in parameter_description:
        if not isinstance(param, str):
            raise Exception('Unexpected type for {param}')
        if param not in signature:
            raise Exception(f'Parameter {param} not in signature of function {original_function}')

    print(parameter_description)

    print(f'signature: {signature}')
    for key in signature:
        print(key)

    return []


# TEST CODE #

@precondition([0, 'second_arg'], is_not_none)
def a_function_requiring_decoration(first_arg, second_arg='') -> str:
    print("Decorated")


a_function_requiring_decoration('test')
