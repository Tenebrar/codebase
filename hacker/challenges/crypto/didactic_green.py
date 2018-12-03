from hacker.decoder import decode
from hacker.images import pixels
from hacker.settings import inputfile

filename = inputfile('crypto', 'didactic_green', 'greenline.png')

result = decode(pixels(filename), lambda x: x[1], chr)
print(result)
