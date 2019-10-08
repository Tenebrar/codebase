from projecteuler.util.number_properties import is_palindrome


def reverse_and_add(number: int) -> int:
    return number + int(str(number)[::-1])


def is_lychrel_number(number: int) -> bool:
    return is_palindrome(reverse_and_add(number))  # TODO


def problem_0055() -> int:
    return sum(1 for i in range(1, 10000) if is_lychrel_number(i))


if __name__ == '__main__':
    print(problem_0055())
    # Expected: 
