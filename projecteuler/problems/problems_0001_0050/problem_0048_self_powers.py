def problem_0048(maximum: int) -> str:  # str because the result might start with a 0
    total = sum(i**i for i in range(1, maximum + 1))
    return str(total)[-10:]


if __name__ == '__main__':
    MAXIMUM = 1000

    print(problem_0048(MAXIMUM))
    # Expected: 9110846700
