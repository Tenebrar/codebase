from util.combinatorics.functions import combination


def problem_0053() -> int:
    total = 0
    for n in range(1, 101):
        for r in range(n):
            if combination(n, r) > 1000000:
                total += 1

    return total


if __name__ == '__main__':
    print(problem_0053())
    # Expected: 4075
