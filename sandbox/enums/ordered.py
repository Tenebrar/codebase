from enum import Enum
from functools import wraps


def comparison_method(original_function):
    """ Implements the default behaviour of returning NotImplemented if the classes of the 2 arguments do not match. """
    @wraps(original_function)
    def wrapped_function(*args, **kwargs):
        if args[0].__class__ is not args[1].__class__:
            return NotImplemented
        return original_function(*args, **kwargs)
    return wrapped_function


class OrderedEnum(Enum):
    """
    Enum allowing comparison methods based on their occurrence in the Enum.
    Usage of @unique is strongly suggested.
    """
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj.__index__ = len(cls.__members__) + 1
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
