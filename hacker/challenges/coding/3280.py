from collections import Counter

from hacker.settings import inputfile

# Source: https://www.rfc-editor.org/rfc/rfc3280.txt
filename = inputfile('coding', '3280', 'rfc3280.txt')

with open(filename, 'r') as file:
    value = file.read()

print(Counter([x for x in value.split() if len(x) == 9]).most_common()[0][0])
