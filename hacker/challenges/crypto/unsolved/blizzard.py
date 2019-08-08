from collections import Counter

from hacker.bytestreams import bytes_from_binary, skip
from hacker.decoder import decode
from hacker.images import pixels, size
from hacker.settings import inputfile
from hacker.util import x_max, x_min

filename = inputfile('crypto', 'blizzard', 'blizzard.png')

width, height = size(filename)
print(width, height)  # 5 * 83, 7 * 47

temp = decode(pixels(filename), lambda p: '1' if p[0] else '0')
print(temp)

print(Counter(temp))

#result = decode(skip(bytes_from_binary(temp, 7), 47), chr)
#print(result)

from PIL import Image

from hacker.decoder import decode, toint2

im = Image.open(filename)
pix = im.load()
width, height = im.size

# IDEA try other "shapes", skipping X bits, etc.
def weight(indices):
    w = 0
    amount = 0
    for j, i in indices:
        w += pix[i, j][0]//255
        amount += 1
    return w / amount


def weight_of_rectangle(col, row, sub_width, sub_height):
    w = 0
    for j in range(row, row + sub_height):
        for i in range(col, col + sub_width):
            w += pix[i, j][0]//255
    return w / (sub_width * sub_height)


def subsections(width_divisions, height_divisions):
    sub_width = width // width_divisions
    sub_height = height // height_divisions
    for k in range(width_divisions):
        for l in range(height_divisions):
            yield k * sub_width, l * sub_height, sub_width, sub_height


for subsection in subsections(5, 7):
    print(weight_of_rectangle(*subsection))

w_div = 5
h_div = 7

print([(x, weight_of_rectangle(*x)) for x in x_max(subsections(w_div, h_div), amount=3, key=lambda s: weight(*s))])
print([(x, weight_of_rectangle(*x)) for x in x_min(subsections(w_div, h_div), amount=3, key=lambda s: weight(*s))])

n = [weight_of_rectangle(*x) for x in subsections(w_div, h_div)]
print(sum(n)/len(n))


# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# temp = decode(alphabet, ord, toint2)
# print(Counter(temp))
# print(112/(112+96))  # So the expected weight for ascii text is 0.53 (0.61 if they are represented with 7 bits)
# print(112/(112+96-26))

# IDEA try averaging out each 5 by 7 section or making the pictures with the pixels 5 and 7 apart
