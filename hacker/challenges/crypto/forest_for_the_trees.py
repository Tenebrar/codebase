from PIL import Image

from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'forest_for_the_trees', 'green.jpg')
outputfilename = outputfile('crypto', 'forest_for_the_trees', 'green2.jpg')

im = Image.open(filename)
im = im.convert('RGB')
pix = im.load()

test = {}

width, height = im.size
for i in range(height):
    for j in range(width):
        test[pix[j, i]] = 0
        pix[j,i] = (0, 255 if pix[j,i][2] else 0, 0)

im.save(outputfilename, 'JPEG')

print('colorblind')