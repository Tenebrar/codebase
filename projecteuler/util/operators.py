from functools import reduce
from operator import mul
from typing import Iterable


def product(inputs: Iterable[int]) -> int:
    """ Given a string of numbers, returns the product of those numbers """
    return reduce(mul, inputs, 1)
