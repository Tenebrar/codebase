from typing import List


def to_factoradic(num: int) -> List[int]:
    # https://en.wikipedia.org/wiki/Factorial_number_system
    result = []

    div = 1
    while num > 0:
        num, remainder = divmod(num, div)
        result.insert(0, remainder)
        div += 1

    return result
