def check(i, power):
    total = 0
    for d in str(i):
        total += int(d) ** power
    return total == i


def problem_0030(power: int) -> int:
    total = 0
    for i in range(10, 1000000):  # TODO clear up this max
        if check(i, power):
            total += i
    return total


if __name__ == '__main__':
    POWER = 5

    print(problem_0030(POWER))
    # Expected: 443839
