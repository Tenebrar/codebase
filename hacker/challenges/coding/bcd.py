from hacker.decoder import decode, int2

value = '0111 0011 1001 0011 1001 0001'

result = decode(value.split(), int2, str)
print(result)
