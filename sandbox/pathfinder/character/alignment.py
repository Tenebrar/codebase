from enum import Enum, unique, auto


@unique
class Alignment(Enum):
    LAWFUL_GOOD = auto()
    TRUE_GOOD = auto()
    CHAOTIC_GOOD = auto()

    LAWFUL_NEUTRAL = auto()
    TRUE_NEUTRAL = auto()
    CHAOTIC_NEUTRAL = auto()

    LAWFUL_EVIL = auto()
    TRUE_EVIL = auto()
    CHAOTIC_EVIL = auto()