from projecteuler.util.divisors import divisors
from projecteuler.util.string_properties import is_palindrome as is_palindrome_string


def is_palindrome(number: int) -> bool:
    return is_palindrome_string(str(number))


def is_amicable(num: int) -> bool:
    """ Returns whether the number is part of an amicable number pair """
    friend = sum(divisors(num)) - num
    # Only those in pairs are amicable numbers. If the sum is the number itself, it's a perfect number
    return friend != num and sum(divisors(friend)) - friend == num


def is_abundant(num: int) -> bool:
    """ Returns whether the number is abundant """
    return sum(divisors(num)) - num > num
