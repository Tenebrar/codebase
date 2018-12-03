from PIL import Image, ImageDraw

from hacker.settings import outputfile

# Replaced the flags with the middle letters in their name; indicating left, right, up and down
value = 'rrlddrruudrdrrulddrrruuurrdllrrddruuurdrdrdruuudddrrrulluurrrdrdrdrurururdrdrdrurururrrllddrldrrruuurrddllrdrrrruuddrrulurldrdrrruuurrllddrldrrrruuulrrldddrrruuurrlldddrrruuudrrudddr'  # noqa

filename_out = outputfile('crypto', 'telecran', 'telecran.png')

im = Image.new('1', (600, 60), 1)
draw = ImageDraw.Draw(im)

row, col = 1, 1
for c in value:
    old_row, old_col = row, col
    if c == 'u':
        row = row - 1
    elif c == 'd':
        row = row + 1
    elif c == 'l':
        col = col - 1
    elif c == 'r':
        col = col + 1

    draw.line((old_col * 10, old_row * 10, col * 10, row * 10))

del draw

im.save(filename_out, "PNG")

print('the answer is etch')
