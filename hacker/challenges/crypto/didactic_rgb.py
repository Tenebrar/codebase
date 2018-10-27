from PIL import Image

from hacker.decoder import decode, toint16
from hacker.settings import inputfile

filename = inputfile('crypto', 'didactic_rgb', 'didactrgb.png')

rgb = Image.open(filename).load()[0, 0]

result = int(decode(rgb, toint16), 16)
print(result)
