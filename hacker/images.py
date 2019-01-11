from PIL import Image


def pixels(imagefile):
    """
    Generates a stream of pixel values for an image file
    :param imagefile: a filename
    :return: a generator of pixel values (RGBA tuples)
    """
    im = Image.open(imagefile)
    pix = im.load()
    width, height = im.size
    for j in range(height):
        for i in range(width):
            yield pix[i, j]


def size(imagefile):
    """ Returns the size of an imagefile as a tuple (width, height) """
    im = Image.open(imagefile)
    return im.size
