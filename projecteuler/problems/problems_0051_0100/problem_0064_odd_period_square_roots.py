from math import sqrt


def _continued_fraction(base: int, addition: int=0, divide: int=1, depth: int =0) -> None:
    if depth > 10:
        return

    value = int((sqrt(base) + addition) / divide)
    print(value)

    # reciprocal = divide / (sqrt(base) + addition - divide * value)
    # reciprocal = sqrt(base) + value / (base - value * value)



    _continued_fraction(base, value, base - value * value, depth + 1)



    # values = []
    # value = sqrt(number)
    # print(int(value))
    #
    # values.append(value)
    #
    # for _ in range(10):
    #     value = 1 / (value - int(value))
    #     print(int(value))
    #
    #     if value in values:
    #         print('FOUND')
    #
    #     values.append(value)
    #     print(values)


def problem_0064() -> int:
    _continued_fraction(23)
    return 0


if __name__ == '__main__':
    print(problem_0064())
    # Expected:
