# Defined as the minimum allowed value of an integer in the hackvm
MIN_INT = -(1 << 63)
# Defined as the maximum allowed value of an integer in the hackvm
MAX_INT = (1 << 63) - 1


def verify_integer(value: int) -> None:
    """
    Verifies an integer falls within the allowed limits
    :param value: an integer value
    :return: None
    :raises: ValueError if the passed value is too small or too large
    """
    if value < MIN_INT or value > MAX_INT:
        raise ValueError(f'Integer overflow: {value}')
