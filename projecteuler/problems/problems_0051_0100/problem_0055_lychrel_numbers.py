from projecteuler.util.number_properties import is_palindrome

MAX_ITERATIONS = 50


def _is_lychrel_number(number: int) -> bool:
    """ Returns whether a number is a Lychrel number (with reasonable certainty) """
    for _ in range(MAX_ITERATIONS):
        number += int(str(number)[::-1])
        if is_palindrome(number):
            return False
    return True


def problem_0055(maximum: int) -> int:
    return sum(1 for i in range(1, maximum) if _is_lychrel_number(i))


if __name__ == '__main__':
    MAXIMUM = 10000

    print(problem_0055(MAXIMUM))
    # Expected: 249
