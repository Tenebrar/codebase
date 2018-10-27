from hacker.bytestreams import bytes_from_hex

value = 'e5534adac53023aaad55518ac42671f8a1471d94d8676ce1b11309c1c27a64b1ae1f4a91c73f2bfce74c5e8e826c27e1f74c4f8081296ff3ee4519968a6570e2aa0709c2c4687eece44a1589903e79ece75117cec73864eebe57119c9e367fefe9530dc1'  # noqa

print('This', end='')  # The key is only used to encode the first 4 characters

byte_list = list(bytes_from_hex(value))

result = ''
for i in range(4, len(byte_list)):
    c = chr(byte_list[i] ^ byte_list[i - 4])
    result += c

print(result)
