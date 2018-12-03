from PIL import Image

from hacker.settings import inputfile, outputfile

filename = inputfile('crypto', 'redeye', 'redeye.jpg')
filename_out = outputfile('crypto', 'redeye', 'redeye2.jpg')

im = Image.open(filename)

r, g, b = im.split()

r.save( filename_out, 'JPEG' )

# In the bottom right corner of the resulting image
print('HAL9000')
