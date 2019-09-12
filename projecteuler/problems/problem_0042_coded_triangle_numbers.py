from projecteuler.settings import inputfile
from projecteuler.util.summation import sum_all_to

TRIANGLE_NUMBERS = [1]  # Will be increased by the _is_triangle_word function as needed


def _letter_value(letter: str) -> int:
    """ Return the (1-based) index of the letter in the alphabet (assumes upper case) """
    return ord(letter) - ord('A') + 1


def _word_value(word: str) -> int:
    """ Returns the word value of the word (sum of its letter values) """
    return sum(map(_letter_value, word))


def _is_triangle_word(word: str) -> bool:
    """ Returns whether a word is a triangle word. Increases TRIANGLE_NUMBERS as needed """
    value = _word_value(word)

    while value > TRIANGLE_NUMBERS[-1]:
        TRIANGLE_NUMBERS.append(sum_all_to(len(TRIANGLE_NUMBERS) + 1))

    return value in TRIANGLE_NUMBERS


def problem_0042(filename: str) -> int:
    with open(inputfile(filename), 'r') as file:
        words = file.read().replace('"', '').split(',')

    return sum(map(_is_triangle_word, words))


if __name__ == '__main__':
    FILENAME = 'p042_words.txt'

    print(problem_0042(FILENAME))
    # Expected: 162

# IDEA I can make a function that checks if a number is a triangle number using the sqrt
# It works in practice for these numbers, but I want to make sure it is theoretically correct

# from math import sqrt
#
#
# def _is_triangle_number(number: int) -> bool:
#     s = int(sqrt(number * 2))
#     return s * (s + 1) == number * 2
#
#
# for i in range(1, 100):
#     if _is_triangle_number(i):
#         print(i in TRIANGLE_NUMBERS)
