from typing import TypeVar

X = TypeVar('Tuple[float, ...]')


def scalar_multiply(t: X, multiplier: float) -> X:
    """
    Multiply a tuple with a scalar
    """
    return tuple(c * multiplier for c in t)
