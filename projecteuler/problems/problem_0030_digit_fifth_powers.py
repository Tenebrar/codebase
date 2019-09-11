from itertools import count


def _is_digit_power_sum(number: int, power: int) -> bool:
    """ Returns whether a number is equal to the sum of its digits to the given power """
    return number == sum(d ** power for d in map(int, str(number)))


def _find_max(power: int) -> int:
    """ Find a theoretical maximum where a number can be equal to the sum of its digits to the given power """
    for digits in count(1):
        maximum = 10 ** digits - 1
        value = 9 ** power * digits

        if maximum > value:
            return value


def problem_0030(power: int) -> int:
    return sum(i for i in range(10, _find_max(power)) if _is_digit_power_sum(i, power))


if __name__ == '__main__':
    POWER = 5

    print(problem_0030(POWER))
    # Expected: 443839
