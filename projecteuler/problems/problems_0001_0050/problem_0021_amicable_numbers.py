from projecteuler.util.number_properties import is_amicable


def problem_0021(maximum: int) -> int:
    return sum(filter(is_amicable, range(1, maximum)))


if __name__ == '__main__':
    MAXIMUM = 10000

    print(problem_0021(MAXIMUM))
    # Expected: 31626
