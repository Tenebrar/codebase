from typing import Iterable


def fibonacci(start_values=(1, 1)) -> Iterable[int]:
    """ Infinite generator of Fibonacci numbers (with an optional parameter to set the starting values) """
    results = list(start_values)
    index = 0

    while True:
        yield results[index]
        results[index] = sum(results)
        index = 1 - index
