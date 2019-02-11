from enum import Enum, unique


# TODO see if I can make a DefaultingEnum and CaseInsensitiveEnum
@unique
class TestEnum(Enum):
    A = 'a'
    B = 'b'
    UNKNOWN = 'unknown'

    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member

        return cls.UNKNOWN


print(TestEnum('a'))
print(TestEnum('A'))
print(TestEnum('test'))
