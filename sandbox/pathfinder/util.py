from typing import Tuple, TypeVar

X = TypeVar('X')


def scalar_multiply(tuple: Tuple[X,...], multiplier: int) -> Tuple[X,...]:
    """
    Multiply a tuple with a scalar while maintaining types
    """
    return (X(c) * multiplier for c in tuple)