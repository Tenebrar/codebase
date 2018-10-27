from hacker.bytestreams import bytes_from_binary
from hacker.decoder import decode
from hacker.settings import inputfile

filename = inputfile('crypto', 'didactic_text_3', 'text.txt')
with open(filename, 'r') as f:
    binary = decode(f.readlines(), lambda line: line[-3:] == '  \n', lambda b: '1' if b else '0')

result = decode(bytes_from_binary(binary), chr)
print(result)
