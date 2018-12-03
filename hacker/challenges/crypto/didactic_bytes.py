from hacker.decoder import decode, toint2

value = [199, 77, 202]

result = int(decode(value, toint2), 2)
print(result)
