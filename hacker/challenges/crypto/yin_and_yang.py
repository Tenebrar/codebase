from PIL import Image

from hacker.settings import inputfile, outputfile

filename1 = inputfile('crypto', 'yin_and_yang', 'masgo-1.gif')
filename2 = inputfile('crypto', 'yin_and_yang', 'masgo-2.gif')

filename_out = outputfile('crypto', 'yin_and_yang', 'masgo-xor.gif')

im1 = Image.open(filename1)
im2 = Image.open(filename2)

im1 = im1.convert('RGB')
im2 = im2.convert('RGB')

pix1 = im1.load()
pix2 = im2.load()

width, height = im1.size
for i in range(height):
    for j in range(width):
        pix1[i,j] = (pix1[i,j][0] ^ pix2[i,j][0], pix1[i,j][1] ^ pix2[i,j][1], pix1[i,j][2] ^ pix2[i,j][2])

im1.save(filename_out, 'JPEG')

# Read from the resulting picture
print('The answer to this challenge is Darmstadt. Greetings from the Technical University of Darmstadt in Germany')
