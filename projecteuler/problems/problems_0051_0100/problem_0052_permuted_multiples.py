from itertools import count


def _same_digits(number) -> bool:
    """ Check that the number has the same digits as its multiples (1-6) """
    base = sorted(str(number))
    for i in range(2, 7):
        if sorted(str(i * number)) != base:
            return False
    return True


def problem_0052():
    for i in count(1):
        if _same_digits(i):
            return i


if __name__ == '__main__':
    print(problem_0052())
    # Expected: 142857
