import re
import requests

FILENAME = 'function_values.txt'


def read_two_numbers_from_file():
    results = {}
    with open(FILENAME, 'r') as file:
        for line in file:
            m = re.search('([0-9]*), ([0-9]*) -> \\[(.*)\\]\n', line)
            one = int(m.group(1))
            two = int(m.group(2))
            numbers = [int(x) for x in m.group(3).split(',')]
            results[(one, two)] = numbers
    return results


results = read_two_numbers_from_file()


def get_two_numbers(one, two):
    if (one, two) in results:
        return results[(one, two)]

    link = f'http://www.hacker.org/challenge/misc/twonumbers.php?one={one}&two={two}&go=Try'
    page = requests.get(link).text
    last_line = page.split()[-1]
    numbers = [int(x) for x in last_line.split('<br>') if x]

    assert len(numbers) == 12

    with open(FILENAME, 'a') as file:
        file.write(f'{one}, {two} -> {numbers}\n')
        results[(one, two)] = numbers

    return numbers


minimum = 1000000000
maximum = -minimum
# function limits seem to be one: [0-999] two:[0-299]
for one in range(1000):
    print(one)
    for two in range(300):
        numbers = get_two_numbers(one, two)

        minimum = min(minimum, min(numbers))
        maximum = max(maximum, max(numbers))

print(f'min: {minimum}, max: {maximum}')
