from typing import Tuple, TypeVar, cast

TF = TypeVar('TF', bound=Tuple[float, ...])


def scalar_multiply(t: TF, multiplier: float) -> TF:
    """
    Multiply a tuple with a scalar
    """
    return cast(TF, tuple(c * multiplier for c in t))
