from hacker.decoder import decode, toint16
from hacker.images import pixels
from hacker.settings import inputfile

filename = inputfile('crypto', 'didactic_red', 'redline.png')

result = decode(pixels(filename), lambda x: x[0], toint16)
print(result)
