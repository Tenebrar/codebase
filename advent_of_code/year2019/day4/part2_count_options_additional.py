from collections import Counter
from typing import Iterable


def digits(integer: int) -> Iterable[int]:
    while integer > 0:
        yield integer % 10
        integer //= 10


count = 0
for password in range(125730,579381 + 1):
    if len(set(digits(password))) > 5:
        continue
    d = list(reversed(list(digits(password))))
    if d != sorted(d):
        continue
    counter = Counter(digits(password))
    if 2 not in counter.values():
        continue

    count += 1

print(count)
