from typing import Any, Iterable, List

PERMUTATION = 1000000
ELEMENTS = [i for i in range(10)]


def to_factoradic(num: int) -> List[int]:
    result = []

    div = 1
    while num > 0:
        num, remainder = divmod(num, div)
        result.insert(0, remainder)
        div += 1

    return result


def permutation(num: int, values: List[Any]) -> Iterable[Any]:
    factoradic = to_factoradic(num - 1)  # Adjust for 0-indexing
    factoradic = [0] * (len(values) - len(factoradic)) + factoradic

    return [values.pop(i) for i in factoradic]


print(''.join(str(i) for i in permutation(PERMUTATION, ELEMENTS)))
# Expected: 2783915460
