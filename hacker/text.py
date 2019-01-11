def remove_punctuation(string):
    """
    Removes all non-letter, non-space characters from a string
    :param string: a string
    :return: a string containing only letters and spaces
    """
    return ''.join([c for c in string if c.isalpha() or c.isspace()])
