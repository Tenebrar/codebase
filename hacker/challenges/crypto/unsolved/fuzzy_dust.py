from PIL import Image

from hacker.bytestreams import ungroup
from hacker.decoder import toint16
from hacker.images import pixels
from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'fuzzy_dust', 'fuzz.bmp')

i = 0
for p in ungroup(pixels(filename)):
    print(toint16(p))
    if i > 100:
        break
    i += 1

filename_out_r = outputfile('crypto', 'fuzzy_dust', 'fuzz_r.jpg')
filename_out_g = outputfile('crypto', 'fuzzy_dust', 'fuzz_g.jpg')
filename_out_b = outputfile('crypto', 'fuzzy_dust', 'fuzz_b.jpg')

im = Image.open(filename)

r, g, b = im.split()

r.save( filename_out_r, 'JPEG' )
g.save( filename_out_g, 'JPEG' )
b.save( filename_out_b, 'JPEG' )
