from enum import Enum


# The different sizes of characters in pathfinder
class Size(Enum):
    FINE = 'Fine'
    DIMINUTIVE = 'Diminutive'
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    HUGE = 'Huge'
    GARGANTUAN = 'Gargantuan'
    COLOSSAL = 'Colossal'


class AlignmentLawAxis(Enum):
    LAWFUL = 'Lawful'
    TRUE = 'True'
    CHAOTIC = 'Chaotic'


class AlignmentGoodAxis(Enum):
    GOOD = 'Good'
    NEUTRAL = 'Neutral'
    EVIL = 'Evil'


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'