from hacker.decoder import decode
from hacker.settings import inputfile

filename = inputfile('crypto', 'didactic_vampire_text', 'text.txt')
with open(filename, 'r') as f:
    value = f.read()

result = decode(filter(str.isupper, value))
print(result)
