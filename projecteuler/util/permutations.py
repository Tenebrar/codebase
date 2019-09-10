from typing import List, Iterable, Any

from projecteuler.util.conversions import to_factoradic


def permutation(num: int, values: List[Any]) -> Iterable[Any]:
    factoradic = to_factoradic(num - 1)  # Adjust for 0-indexing
    factoradic = [0] * (len(values) - len(factoradic)) + factoradic

    return [values.pop(i) for i in factoradic]
