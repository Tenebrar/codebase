from sandbox.enums.enums import OrderedEnum
from enum import auto


# The different sizes of characters in pathfinder
class Size(OrderedEnum):
    FINE = auto()
    DIMINUTIVE = auto()
    TINY = auto()
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    HUGE = auto()
    GARGANTUAN = auto()
    COLOSSAL = auto()
