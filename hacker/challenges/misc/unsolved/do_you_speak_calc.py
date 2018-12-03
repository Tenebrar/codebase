from hacker.decoder import decode, int2

value = '1100111 0001110 1001111 1110111 1011011 1001111 0000000 0001111 0100111 1100111 1001111 0000000 0100000 1011011 1001110 0110000 1001111 0010101 0001111 0110000 1000111 0110000 1001110 0000010'  # noqa

result = decode(value.split(), int2, chr)
print(result)

result = decode(value.split(), int2, str, lambda x: x + ' ')
print(result)
