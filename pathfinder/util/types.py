from typing import Any, Tuple, TypeVar


def scalar_multiply(t: Tuple[Any, ...], multiplier: float) -> Tuple[Any, ...]:
    """
    Multiply a tuple with a scalar while maintaining types
    """
    return tuple(c * multiplier for c in t)
