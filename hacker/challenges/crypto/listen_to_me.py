from PIL import Image

from hacker.bytestreams import ungroup
from hacker.decoder import transform
from hacker.images import pixels
from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'listen_to_me', 'listen.png')
outputfilename = outputfile('crypto', 'listen_to_me', 'listen.raw')

with open(outputfilename, 'wb') as output_file:
    im = Image.open(filename)
    output_file.write(bytes(ungroup(transform(pixels(filename), lambda p: p[:3]))))

# The result are raw sound values. Playing the resulting sound file, it says:
print('1234')
