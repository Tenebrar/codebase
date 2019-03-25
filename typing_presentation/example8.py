# Mypy understands several checks
from typing import Optional


def foo(o: object) -> None:
    print(o + 5)  # Error: can't add 'object' and 'int'

    if isinstance(o, int):
        print(o + 5)

    assert isinstance(o, int)
    print(o + 5)


def foo2(o: Optional[str]):
    o.splitlines()  # Error: None has no attribute "splitlines"

    if o is not None:
        o.splitlines()
