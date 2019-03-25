from typing import Dict, List, Set, Tuple

a: int = 1
b: float = 1.0
c: bool = True
d: str = "test"
e: bytes = b"test"

f: List[int] = [1]
g: Set[int] = {6, 7}

h: Dict[str, float] = {'field': 2.0}

i: Tuple[int, str, float] = (3, "yes", 7.5)


def my_add(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float
