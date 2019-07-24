from hacker.bytestreams import ungroup, bytes_from_binary
from hacker.decoder import transform, decode
from hacker.images import pixels
from hacker.settings import inputfile, outputfile
from PIL import Image

filename = inputfile('crypto', 'filtration_residue', 'residue.png')
outputfilename = outputfile('crypto', 'filtration_residue', 'residue2.png')

im = Image.open(filename)
im = im.convert('RGB')
pix = im.load()

mod_val = 16
div_val = mod_val - 1

width, height = im.size
for i in range(height):
    for j in range(width):
        pix[j,i] = ((pix[j,i][0] % mod_val) * (255//div_val), (pix[j,i][1] % mod_val) * (255//div_val), (pix[j,i][2] % mod_val) * (255//div_val))

im.save(outputfilename, 'PNG')

# for p in ungroup(pixels(filename)):
#    print(p%2, end='')

# TODO Look at text chunks
# Source: https://github.com/ctfs/write-ups-2015/tree/master/confidence-ctf-teaser-2015/stegano/a-png-tale-200
# TODO find out why it fails and what that means
from struct import unpack
from binascii import hexlify, unhexlify
import sys, zlib

# Returns [Position, Chunk Size, Chunk Type, Chunk Data, Chunk CRC]
def getChunk(buf, pos):
    a = []
    a.append(pos)
    size = unpack('!I', buf[pos:pos+4])[0]
    # Chunk Size
    a.append(buf[pos:pos+4])
    # Chunk Type
    a.append(buf[pos+4:pos+8])
    # Chunk Data
    a.append(buf[pos+8:pos+8+size])
    # Chunk CRC
    a.append(buf[pos+8+size:pos+12+size])
    return a

def printChunk(buf, pos):
    print('Pos : '+str(pos)+'')
    print('Type: ' + str(buf[pos+4:pos+8]))
    size = unpack('!I', buf[pos:pos+4])[0]
    print('Size: ' + str(size))
    # print 'Cont: ' + str(hexlify(buf[pos+8:pos+8+size]))
    print('CRC : ' + str(hexlify(buf[pos+size+8:pos+size+12]).upper()))
    print()


buf = open(filename, 'rb').read()
pos=0

print("PNG Signature: " + str(unpack('cccccccc', buf[pos:pos+8])))
pos+=8

chunks = []
for i in range(3):
    chunks.append(getChunk(buf, pos))
    printChunk(buf, pos)
    pos+=unpack('!I',chunks[i][1])[0]+12

# http://hoshi-sano.hatenablog.com/entry/2013/08/18/113434
decompressed = zlib.decompress(chunks[1][3])
# Decompressed data length = height x (width * 3 + 1)
print("Data length in PNG file : ", len(chunks[1][3]))
print("Decompressed data length: ", len(decompressed))

height = unpack('!I',(chunks[0][3][4:8]))[0]
width = unpack('!I',(chunks[0][3][:4]))[0]
blocksize = width * 3 + 1
filterbits = ''
for i in range(0,len(decompressed),blocksize):
    bit = unpack('2401c', decompressed[i:i+blocksize])[0]
    if bit == '\x00': filterbits+='0'
    elif bit == '\x01': filterbits+='1'
    else:
        print('Bit is not 0 or 1... Default is 0 - MAGIC!')
        sys.exit(3)

s = filterbits
endianess_filterbits = [filterbits[i:i+8][::-1] for i in range(0, len(filterbits), 8)]

flag = ''
for x in endianess_filterbits:
    if x=='00000000': break
    flag += unhexlify('%x' % int('0b'+str(x), 2)).decode('utf-8')

print('Flag: ' + flag)
