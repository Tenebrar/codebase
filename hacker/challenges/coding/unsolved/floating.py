from struct import pack, unpack

value = 0b01000001000010001010001011000000

b = pack('i', value)
res = unpack('f', b)

print(res)
