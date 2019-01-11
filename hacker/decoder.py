def int16(c):
    """ Parse a string as a hexadecimal number """
    return int(c, 16)


def toint16(i):
    """ Convert a number to a hexadecimal string of length 2 """
    return f'{i:02x}'


def int2(c):
    """ Parse a string as a binary number """
    return int(c, 2)


def toint2(i):
    """ Convert a number to a binary string of length 8 """
    return f'{i:08b}'


def transform(stream, *args):
    """
    Takes a stream of elements and returns a stream of transformed elements.
    Each element of the original stream is passed through all the transformations in order and then returned.
    Transformations can be either functions taking a single argument and returning a single value, or dicts, in which
    case the transformation is the retrieval of the value in the dict (defaulting to the original value if not present)
    :param stream: a generator
    :param args: Transformations (functions or dicts)
    :return: a generator of transformed objects
    """
    for value in stream:
        for transformation in args:
            if isinstance(transformation, dict):
                value = transformation.get(value, value)
            else:
                value = transformation(value)
        yield value


def decode(stream, *args):
    """
    Takes a stream of elements and returns a string made up of transformed elements.
    Each element of the original stream is passed through all the transformations in order and then joined in a string.
    Transformations can be either functions taking a single argument and returning a single value, or dicts, in which
    case the transformation is the retrieval of the value in the dict (defaulting to the original value if not present)
    :param stream: a generator
    :param args: Transformations (functions or dicts)
    :return: a string joining the transformed objects
    """
    return ''.join(transform(stream, *args))
