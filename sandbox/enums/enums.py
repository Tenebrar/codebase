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
    Enum allowing comparison methodes based on their occurrence in the Enum.
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


# @unique
# class Planet(OrderedEnum):
#     """ Example usage of OrderedEnum """
#     MERCURY = (3.303e+23, 2.4397e6)
#     VENUS = (4.869e+24, 6.0518e6)
#     EARTH = (5.976e+24, 6.37814e6)
#     MARS = (6.421e+23, 3.3972e6)
#     JUPITER = (1.9e+27, 7.1492e7)
#     SATURN = (5.688e+26, 6.0268e7)
#     URANUS = (8.686e+25, 2.5559e7)
#     NEPTUNE = (1.024e+26, 2.4746e7)
#
#     # universal gravitational constant  (m3 kg-1 s-2)
#     __G__ = 6.67300E-11  # Needs double underscores, or it would be considered another Planet
#
#     def __init__(self, mass, radius):
#         self.mass = mass  # in kilograms
#         self.radius = radius  # in meters
#
#     def __repr__(self):
#         return self.name
#
#     @property
#     def surface_gravity(self):
#         return self.__G__ * self.mass / (self.radius ** 2)
