from functools import reduce
from numpy.core.test_rational import lcm

MAXIMUM = 20

print(reduce(lcm, range(1, MAXIMUM)))
# Expected: 232792560
