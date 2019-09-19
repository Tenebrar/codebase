from projecteuler.util.string_properties import is_palindrome


def problem_0036(maximum: int) -> int:
    return sum(i for i in range(1, maximum + 1, 2) if is_palindrome(str(i)) and is_palindrome(f'{i:b}'))


if __name__ == '__main__':
    MAXIMUM = 1000000

    print(problem_0036(MAXIMUM))
    # Expected: 872187
