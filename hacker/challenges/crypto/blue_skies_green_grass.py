from PIL import Image

from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'blue_skies_green_grass', 'blueskies.png')
outputfilename = outputfile('crypto', 'blue_skies_green_grass', 'blueskies2.png')

im = Image.open(filename)
im = im.convert('RGB')
pix = im.load()

width, height = im.size
for i in range(height):
    for j in range(width):
        pix[j,i] = (255 if pix[j,i][0] else 0, 0, 0)

im.save(outputfilename, 'PNG')
