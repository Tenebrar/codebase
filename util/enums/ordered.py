from enum import Enum
from functools import wraps


def comparison_method(original_function):
    """
    Comparison methods should return NotImplemented if the comparison is not supported for both types.
    This decorator implements that default behaviour assuming the comparison is only supported within the same exact
    type.
    """
    @wraps(original_function)
    def wrapped_function(*args, **kwargs):
        if args[0].__class__ is not args[1].__class__:
            return NotImplemented
        return original_function(*args, **kwargs)
    return wrapped_function


class OrderedEnum(Enum):
    """
    Enum allowing comparison methods based on the order of their occurrence in the Enum.
    Usage of @unique is strongly recommended.
    """
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj.__index__ = len(cls.__members__)
        return obj

    @comparison_method
    def __lt__(self, other):
        return self.__index__ < other.__index__

    @comparison_method
    def __gt__(self, other):
        return self.__index__ > other.__index__

    @comparison_method
    def __le__(self, other):
        return self.__index__ <= other.__index__

    @comparison_method
    def __ge__(self, other):
        return self.__index__ >= other.__index__
