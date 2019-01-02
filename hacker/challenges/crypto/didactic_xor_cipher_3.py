from hacker.bytestreams import bytes_from_hex

value = '31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588'


def decode(ciphertext, key1, key2):
    """ Decode the ciphertext with the 2 keys """
    plaintext = ''
    for b in bytes_from_hex(ciphertext):
        plaintext += chr(b ^ key1)
        key1 = (key1 + key2) % 256

    return plaintext

for i in range(256):
    for j in range(256):
        result = decode(value, i, j)
        if result.isprintable() and 'the' in result:
            print(result)
