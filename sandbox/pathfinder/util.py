from typing import TypeVar

X = TypeVar('Tuple[float, ...]')  # Not sure this is correct, should it be TypeVar('X', bound=Tuple...) or similar?


def scalar_multiply(t: X, multiplier: float) -> X:
    """
    Multiply a tuple with a scalar
    """
    return tuple(c * multiplier for c in t)
