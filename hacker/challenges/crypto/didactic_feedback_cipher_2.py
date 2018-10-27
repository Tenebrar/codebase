from hacker.bytestreams import bytes_from_hex

value = '310a7718781f734c31425e775a314f3b40132c5122720599b2dfb790fd8ff894add2a4bdc5d1a6e987a0ed8eee94adcfbb94ee88f382127819623a404d3f'  # noqa


def decode(ciphertext, key):
    """ Decode as defined by the feedback cipher """
    k = 0x31 ^ ord('I')  # Key is only relevant for first character
    plaintext = ''
    for b in bytes_from_hex(ciphertext):
        c = chr(b ^ k)
        plaintext += c
        k = (b + key) % 0x100
    return plaintext

# Try all the keys
for x in range(256):
    result = decode(value, x)

    if result.isprintable() and 'the' in result:
        print(result)
