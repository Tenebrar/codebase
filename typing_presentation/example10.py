from typing import Iterable, Protocol


def loop(l: Iterable[str]):
    for s in l:
        print(s)


# Protocol
class SupportsRead(Protocol):
    def read(self, amount: int) -> bytes: ...


def r(readable: SupportsRead):
    readable.read(5)
