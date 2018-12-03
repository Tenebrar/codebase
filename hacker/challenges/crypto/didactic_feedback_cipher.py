from hacker.bytestreams import substrings

value = '751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24'

key = ord('Y') ^ 0x75  # Key is only relevant for first character

result = ''
for s in substrings(value, 2):
    v = int(s, 16)
    result += chr(v ^ key)
    key = v

print(result)
