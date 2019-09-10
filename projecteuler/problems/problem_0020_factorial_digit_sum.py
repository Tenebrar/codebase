from math import factorial


def problem_0020(number: int) -> int:
    return sum(map(int, f'{factorial(number)}'))


if __name__ == '__main__':
    NUMBER = 100

    print(problem_0020(NUMBER))
    # Expected: 648
