from enum import Enum, unique, auto


@unique
class Gender(Enum):
    FEMALE = auto()
    MALE = auto()
