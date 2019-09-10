def problem_0029(maximum: int) -> int:
    powers = set()
    for a in range(2, maximum + 1):
        for b in range(2, maximum + 1):
            powers.add(a ** b)

    return len(powers)


if __name__ == '__main__':
    MAXIMUM = 100

    print(problem_0029(MAXIMUM))
    # Expected: 9183
