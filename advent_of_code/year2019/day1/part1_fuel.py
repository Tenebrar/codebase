from advent_of_code.util import input_file


def fuel(mass: int) -> int:
    """ Calculate needed fuel based on mass """
    return mass // 3 - 2


with input_file() as file:
    print(sum(fuel(int(line)) for line in file))
