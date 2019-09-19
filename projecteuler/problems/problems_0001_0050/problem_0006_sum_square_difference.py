from projecteuler.util.summation import sum_all_to, square_pyramidal_number


def problem_0006(amount: int) -> int:
    square_of_sum = sum_all_to(amount) ** 2
    sum_of_squares = square_pyramidal_number(amount)

    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    AMOUNT = 100

    print(problem_0006(AMOUNT))
    # Expected: 25164150
