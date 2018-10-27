from hacker.settings import inputfile

filename = inputfile('crypto', 'steganographic', 'boxes.gif')
with open(filename, 'rb') as f:
    value = f.read()

result = value[-14:-2]
print(result)
