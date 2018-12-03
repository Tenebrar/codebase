from PIL import Image
import math

from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'white_noise', 'whitenoise.png')
filename_out1 = outputfile('crypto', 'white_noise', 'whitenoise_out1.png')
filename_out_prime = outputfile('crypto', 'white_noise', 'whitenoise_out_prime.png')

im = Image.open(filename)

# Set the first index in the palette (this outputs an image with a hint)
palette = bytearray(256*3)
palette[:3] = [255, 255, 255]
im.putpalette(palette)

im.save(filename_out1, 'PNG')


def is_prime(number):
    """ Returns whether the passed integer is a prime number """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    if number == 3:
        return True
    for j in range(3, int(math.sqrt(number)) + 1):
        if number % j == 0:
            return False
    return True

# Set the prime numbers
palette = bytearray(256*3)
for i in range(256):
    if is_prime(i + 1):
        palette[i*3:i*3+3] = [255, 255, 255]
im.putpalette(palette)

im.save(filename_out_prime, 'PNG')

print('The solution is worldofprimenoise')
