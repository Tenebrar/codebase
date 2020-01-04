from advent_of_code.util import input_file


def substrings(string, size):
    """
    Returns the substrings of a string of a given size.
    If the length of the string is not a multiple of size, a smaller string will be returned at the end.
    :param string: a string
    :param size: The desired size of the substrings
    :return: a generator returning the substrings of desired size
    """
    for i in range(0, len(string), size):
        yield string[i:i + size]


with input_file() as file:
    image = file.readline().strip()

LAYER_SIZE = 25 * 6

min_layer = min(substrings(image, LAYER_SIZE), key=lambda layer: layer.count('0'))

print(min_layer.count('1') * min_layer.count('2'))
