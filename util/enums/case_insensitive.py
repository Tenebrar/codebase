from enum import Enum


class CaseInsensitiveEnum(Enum):
    """
    Enum that when a value is called for that is not known, will check if the value would be known when case insensitive
    comparison is done
    """
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member

        return super()._missing_(value)
