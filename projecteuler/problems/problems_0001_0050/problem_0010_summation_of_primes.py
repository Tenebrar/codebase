from util.primes import primes_until


def problem_0010(maximum: int) -> int:
    return sum(primes_until(maximum))


if __name__ == '__main__':
    MAXIMUM = 2000000

    print(problem_0010(MAXIMUM))
    # Expected: 142913828922
