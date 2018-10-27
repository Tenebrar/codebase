from hacker.bytestreams import bytes_from_hex
from hacker.decoder import decode

value = '3d2e212b20226f3c2a2a2b'
key = 79

result = decode(bytes_from_hex(value), lambda b: b ^ key, chr)
print(result)
