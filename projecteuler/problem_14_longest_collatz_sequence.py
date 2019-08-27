from functools import wraps

MAX_STARTING_NUMBER = 1000000


def cached(decorated_function):
    """ Decorator that provides caching to a function """
    cache = {}

    @wraps(decorated_function)
    def function_with_cache(*args):
        try:
            return cache[args]
        except KeyError:
            result = decorated_function(*args)
            cache[args] = result
            return result
    return function_with_cache


@cached
def collatz_sequence_length(num: int) -> int:
    """ Returns the length of the Collatz sequence starting at a given number """
    if num == 1:
        return 1

    if num % 2 == 0:
        return collatz_sequence_length(num // 2) + 1
    else:
        return collatz_sequence_length(3 * num + 1) + 1


print(max(((i, collatz_sequence_length(i)) for i in range(1, MAX_STARTING_NUMBER)), key=lambda x: x[1])[0])
# Expected: 837799
