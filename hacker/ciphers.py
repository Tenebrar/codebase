def rot(char, rot_val):
    """
    Applies the common rotation cipher to a single character
    :param char: a character (non-letters will be returned unchanged)
    :param rot_val: The value by whihch to rotate the letter
    :return: The rotated letter (or unchanged value if not a letter)
    """
    if not char.isalpha():
        return char

    a_value = ord('a') if char.islower() else ord('a')

    return chr( (ord(char) - a_value + rot_val) % 26 + a_value)
