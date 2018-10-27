from hacker.images import pixels
from hacker.settings import inputfile

filename = inputfile('crypto', 'butterfly_effect', 'butterfly.png')

for p in pixels(filename):
    print(p)

# TODO This reminds me of mandelbrot stuff? Not sure there's something to be done with that
