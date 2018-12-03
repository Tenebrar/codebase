def x_max(iterable, amount=1, key=None):
    """
    Returns the largest items in the input

    :param iterable: An iterable
    :param amount: The amount of results
    :param key: The key with which to compare items
    :return: An iterable containing the 'amount' largest items in the 'iterable'
    """
    return sorted(list(iterable), key=key)[:-amount-1:-1]


def x_min(iterable, amount=1, key=None):
    """
    Returns the smallest items in the input

    :param iterable: An iterable
    :param amount: The amount of results
    :param key: The key with which to compare items
    :return: An iterable containing the 'amount' smallest items in the 'iterable'
    """
    return sorted(list(iterable), key=key)[:amount]
