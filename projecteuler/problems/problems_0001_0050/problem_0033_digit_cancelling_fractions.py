from math import gcd

from projecteuler.util.enumeration import digit_range


def _is_digit_cancelling_fraction(numerator: int, denominator: int) -> bool:
    """
    Returns whether the passed fraction is equal to the fraction made up of the first digit of the numerator and the
    second digit of the denominator
    """
    digit00 = numerator // 10
    digit01 = numerator % 10
    digit10 = denominator // 10
    digit11 = denominator % 10

    # Converted the fraction comparisons to product comparisons to avoid rounding errors
    return digit01 == digit10 and digit11 != 0 and numerator * digit11 == digit00 * denominator


def problem_0033() -> int:
    result_numerator = 1
    result_denominator = 1

    # I'm looping over unneeded options, but it does not affect the speed
    # (e.g. I could loop only over those pairs with the same middle digits)
    for numerator in digit_range(2):
        for denominator in range(numerator + 1, 100):  # fraction less than 1
            if _is_digit_cancelling_fraction(numerator, denominator):
                result_numerator *= numerator
                result_denominator *= denominator

    return result_denominator // gcd(result_numerator, result_denominator)


if __name__ == '__main__':
    print(problem_0033())
    # Expected: 100
