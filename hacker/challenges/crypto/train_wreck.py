value = 'iuoa e kcet lheiny wirlwfrb nriswr opc  ihr hywudcos hsoe orase sbiasoe. y letiap,eo ot .unr dhr'

# Shows the idea behind the cipher
for c in value[:24]:
    print(c, end='   ')
print()
print(' ', end='')
for c in value[24:-24]:
    print(c, end=' ')
print()
print('  ', end='')
for c in value[-24:]:
    print(c, end='   ')
print()
print()

# Does the actual decoding
result = [''] * 96
result[::4] = value[:24]
result[1::2] = value[24:-24]
result[2::4] = value[-24:]
print(''.join(result))
