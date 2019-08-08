from itertools import takewhile
from typing import Iterable

# The golden ratio approximation could be used, but I felt these numbers were too small to warrant it

# The sequence has a repeating pattern of 'odd, odd, even', but there seems to be no real way of using that
# It could avoid the modulo check for evenness, but it's not like that is such a heavy operation anyway

MAXIMUM = 4000000


def fibonacci(start_values=(1, 1)) -> Iterable[int]:
    """ Infinite generator of Fibonacci numbers (with an optional parameter to set the starting values) """
    results = list(start_values)
    index = 0

    while True:
        yield results[index]
        results[index] = sum(results)
        index = 1 - index


# Starting the sequence with these numbers is strange to me, but that is the assignment
print(sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x <= MAXIMUM, fibonacci((1,2))))))
# Expected: 4613732
