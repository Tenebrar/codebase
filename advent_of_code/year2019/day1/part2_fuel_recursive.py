from advent_of_code.util import input_file


def fuel(mass: int) -> int:
    return mass // 3 - 2


def fuel_recursive(mass: int) -> int:
    f = fuel(mass)

    if f <= 0:
        return 0

    return f + fuel_recursive(f)


with input_file() as file:
    print(sum(fuel_recursive(int(line)) for line in file))
