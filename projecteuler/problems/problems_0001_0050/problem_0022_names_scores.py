from projecteuler.settings import inputfile


def _score(index, name) -> int:
    # Adjust for 0-index
    return (index + 1) * sum(map(lambda c: ord(c) - ord('A') + 1, name.upper()))


def problem_0022(filename: str) -> int:
    with open(inputfile(filename), 'r') as file:
        names = file.read().replace('"', '').split(',')

    names.sort()

    return sum(_score(index, name) for index, name in enumerate(names))


if __name__ == '__main__':
    FILENAME = 'p022_names.txt'

    print(problem_0022(FILENAME))
    # Expected: 871198282
