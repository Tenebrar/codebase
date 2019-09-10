def sum_all_to(num: int) -> int:
    """ Return the sum of all numbers up to and including the input number """
    return num * (num + 1) // 2


def square_pyramidal_number(num: int) -> int:
    """ Return the sum of the squares of all numbers up to and including the input number """
    # https://en.wikipedia.org/wiki/Square_pyramidal_number
    return num * (num + 1) * (2 * num + 1) // 6
