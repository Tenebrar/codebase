from projecteuler.settings import inputfile


def score(index, name) -> int:
    # Adjust for 0-index
    return (index + 1) * sum(map(lambda c: ord(c) - ord('A') + 1, name.upper()))


with open(inputfile('p022_names.txt'), 'r') as file:
    NAMES = file.read().replace('"', '').split(',')

NAMES.sort()
print(sum(score(index, name) for index, name in enumerate(NAMES)))
# Expected: 871198282
