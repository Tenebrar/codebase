from hacker.bytestreams import ungroup, bytes_from_binary
from hacker.decoder import transform, decode
from hacker.images import pixels
from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'lucy_in_the_sky_with_briolettes', 'briolette.png')
outputfilename = outputfile('crypto', 'lucy_in_the_sky_with_briolettes', 'briolette.txt')

temp = decode(ungroup(transform(pixels(filename), lambda p: p[:3])), lambda v: v % 2, str)
print(temp)
print(len(temp) % 8)

print(min(bytes_from_binary(temp, 5)))
print(max(bytes_from_binary(temp, 5)))

with open(outputfilename, 'wb') as output:
    output.write(bytes(bytes_from_binary(temp)))

result = decode(bytes_from_binary(temp, 10), lambda s: s % 128, chr)
print('START')
i = 0
for c in result:
    if 32 <= ord(c) <= 126:
        print(c, end='')
    else:
        print(f'<{ord(c):02x}>', end='')
    i += 1
    if i % 24 == 0:
        print()
print()
print('END')

from PIL import Image

outputfilename = outputfile('crypto', 'lucy_in_the_sky_with_briolettes', 'briolette2.png')

im1 = Image.new('1', (80*3, 128), 1)

im1 = im1.convert('RGB')
pix1 = im1.load()

im2 = Image.open(filename)
im2 = im2.convert('RGB')
pix2 = im2.load()


print(im1.size)

width, height = im1.size
for i in range(height):
    for j in range(width):
        pix1[j,i] = ((pix2[j//3,i//3][j % 3] % 2) * 255, (pix2[j//3,i//3][j % 3] % 2) * 255, (pix2[j//3,i//3][j % 3] % 2) * 255)

im1.save(outputfilename, 'PNG')
