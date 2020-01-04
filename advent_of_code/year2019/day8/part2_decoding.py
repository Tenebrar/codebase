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

rendered = ['2'] * LAYER_SIZE

for layer in substrings(image, LAYER_SIZE):
    for i in range(len(layer)):
        if rendered[i] == '2':
            rendered[i] = layer[i]

for row in substrings(rendered, 25):
    print(''.join(row).replace('1', '#').replace('0', ' '))
