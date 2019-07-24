from enum import Enum


class DefaultingEnum(Enum):
    """
    Enum that when a value is called for that is not known, a default Enum value is returned instead of raising an
    Exception
    """
    @classmethod
    def get_default(cls):
        return list(cls)[-1]  # Returns the last option by default, this can be changed by overriding this function

    @classmethod
    def _missing_(cls, value):
        return cls.get_default()
