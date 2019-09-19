def problem_0016(exponent: int) -> int:
    return sum(map(int, f'{2 ** exponent}'))


if __name__ == '__main__':
    EXPONENT = 1000

    print(problem_0016(EXPONENT))
    # Expected: 1366
