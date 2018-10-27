# Defined as the minimum allowed value of an integer in the hackvm
MIN_INT = -(1 << 63)
# Defined as the maximum allowed value of an integer in the hackvm
MAX_INT = (1 << 63) - 1


def verify_integer(i):
    """
    Verifies an integer falls within the allowed limits
    :param i: an integer value
    :return: None
    :raises: ValueError if the passed value is too small or too large
    """
    if i < MIN_INT or i > MAX_INT:
        raise ValueError('Integer overflow: {}'.format(i))
