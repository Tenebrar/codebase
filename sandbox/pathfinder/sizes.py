from sandbox.enums.enums import OrderedEnum


# The different sizes of characters in pathfinder
class Size(OrderedEnum):
    FINE = -4
    DIMINUTIVE = -3
    TINY = -2
    SMALL = -1
    MEDIUM = 0
    LARGE = 1
    HUGE = 2
    GARGANTUAN = 3
    COLOSSAL = 4
