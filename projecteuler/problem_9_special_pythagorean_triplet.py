from math import sqrt
from typing import Iterable, Tuple

SUM = 1000

for a in range(1, 1000):
    for b in range(a, 1000):
        c = SUM - a - b
        if a * a + b * b == c * c:
            print(a * b * c)

# Expected: 31875000 (from 200 375 425)

# Even when solved it comes down to a factorization of 500,000
# a + b + c = 1000
# a**2 + b**2 = c**2
# It follows:
# a**2 + b**2 = (1000 - b - a)**2
# a**2 + b**2 = 1,000,000 - 1000b - 1000a - 1000b + b**2 + ab - 1000a + ab + a**2
# a**2 + b**2 = 1,000,000 - 2000a - 2000b + 2ab + a**2 + b**2
# 1,000,000 - 2000a - 2000b + 2ab = 0
# 500,000 - 1000a - 1000b + ab = 0
# 1000a - ab = 500,000 - 1000b
# (1000 - b)a = 500,000 - 1000b
# a = (500,000 - 1000b)/(1000 - b)
# a = 1000(-500 + 1000 - b)/(1000 - b)
# a = -500,000/(1000 - b) + 1000
# (1000 - a)(1000 - b) = 500,000
# The solution below is faster than the original, but it is less clear why it is correct.


def divisors(number) -> Iterable[Tuple[int, int]]:
    for x in range(1, int(sqrt(number))):
        if number % x == 0:
            yield x, number // x


for x, y in divisors(500000):
    a = 1000 - x
    b = 1000 - y
    c = SUM - a - b
    if a > 0 and b > 0 and c > 0:
        print(a * b * c)