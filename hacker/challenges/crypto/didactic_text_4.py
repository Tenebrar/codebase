from hacker.bytestreams import bytes_from_binary
from hacker.decoder import decode
from hacker.settings import inputfile
from hacker.text import remove_punctuation

filename = inputfile('crypto', 'didactic_text_4', 'text.txt')
with open(filename, 'r') as file:
    value = file.read()

value = remove_punctuation(value).lower()

translation = {
    'he': 0,
    'him': 0,
    'his': 0,
    'himself': 0,

    'she': 1,
    'her': 1,
    'hers': 1,
    'herself': 1,
}

binary = decode(filter(lambda w: w in translation, value.split()), translation, str)

result = decode(bytes_from_binary(binary), chr)
print(result)
