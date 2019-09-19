from projecteuler.util.divisors import extract_exponent_of_two_divisor, num_divisors


def problem_0012(wanted_number_of_divisors: int) -> int:
    # We calculate the number of divisors of n*(n+1)/2 based on the number for n and (n+1) to speed up our calculations
    n = 1
    divisors_n = 1

    while True:
        n_plus_one = n + 1
        divisors_n_plus_one = num_divisors(n_plus_one)

        # One of n or (n+1) is odd anyway
        two_pow = extract_exponent_of_two_divisor(n) + extract_exponent_of_two_divisor(n_plus_one)

        # 2 consecutive numbers have no shared divisors, so the number of divisors of the product is the product of the
        # number of divisors
        # The calculation for the number of divisors for a number divided by 2 is based on method 1 from
        # https://www.quora.com/What-is-the-total-number-of-divisors-of-600
        divisors_triangle = divisors_n * divisors_n_plus_one // (two_pow + 1) * two_pow

        if divisors_triangle > wanted_number_of_divisors:
            return n * n_plus_one // 2

        n = n_plus_one
        divisors_n = divisors_n_plus_one


if __name__ == '__main__':
    WANTED_NUMBER_OF_DIVISORS = 500

    print(problem_0012(WANTED_NUMBER_OF_DIVISORS))
    # Expected: 76576500
