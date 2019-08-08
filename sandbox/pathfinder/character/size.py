from enum import auto

from util.enums import OrderedEnum


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
