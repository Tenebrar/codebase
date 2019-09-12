from itertools import count


def _get_pandigital_multiple(number: int) -> int:
    """
    Returns the pandigital number formed by concatening multiples of the given number (or 0 if it does not exist)
    """
    candidate = str(number)
    for i in count(2):
        candidate += str(number * i)
        if len(candidate) >= 9:
            break

    if sorted(candidate) != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return 0

    return int(candidate)


def problem_0038() -> int:
    return max(_get_pandigital_multiple(i) for i in range(1, 10000))


if __name__ == '__main__':
    print(problem_0038())
    # Excepted: 932718654
