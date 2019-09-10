from typing import Sequence


def is_palindrome(sequence: Sequence) -> bool:
    """ Returns whether a sequence is a palindrome """
    return sequence[0:len(sequence) // 2] == sequence[-1:(len(sequence) - 1) // 2:-1]
