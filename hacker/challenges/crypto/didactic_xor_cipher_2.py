from hacker.bytestreams import bytes_from_hex
from hacker.decoder import decode

value = '948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381'

for key in range(0xff):
    result = decode(bytes_from_hex(value), lambda b: b ^ key, chr)
    if result.isprintable() and 'this' in result:
        print(result)
