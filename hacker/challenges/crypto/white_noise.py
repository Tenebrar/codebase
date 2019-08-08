from PIL import Image

from hacker.settings import inputfile, outputfile
from util.primes import is_prime

filename = inputfile('crypto', 'white_noise', 'whitenoise.png')
filename_out1 = outputfile('crypto', 'white_noise', 'whitenoise_out1.png')
filename_out_prime = outputfile('crypto', 'white_noise', 'whitenoise_out_prime.png')

im = Image.open(filename)

# Set the first index in the palette (this outputs an image with a hint)
palette = bytearray(256*3)
palette[:3] = [255, 255, 255]
im.putpalette(palette)

im.save(filename_out1, 'PNG')

# Set the prime numbers
palette = bytearray(256*3)
for i in range(256):
    if is_prime(i + 1):
        palette[i*3:i*3+3] = [255, 255, 255]
im.putpalette(palette)

im.save(filename_out_prime, 'PNG')

print('The solution is worldofprimenoise')
