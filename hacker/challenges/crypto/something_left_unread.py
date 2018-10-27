from hacker.decoder import decode

value = 'KYHP SN TNU KHIP PN ENNV XNM? NX QNUMJL NIL GHJJKNMS QNBLMLS CI GCELJ NX INIJLIJLJ. WUP WHS EUQV XNM TNUM ZULJP HFHCI, OURGCIF DLWMH CJ IN GNJJCWEL VLT, INM ATENGYNIL NM HITPYCIF LEJL.'  # noqa

translation = {
    'H': 'a',
    'W': 'b',
    'Q': 'c',
    'S': 'd',
    'L': 'e',
    'X': 'f',
    'F': 'g',
    'Y': 'h',
    'C': 'i',  # Look at the keys starting from here (will be made clear in the rest of the code)
    'O': 'j',
    'V': 'k',
    'E': 'l',
    'R': 'm',
    'I': 'n',
    'N': 'o',
    'G': 'p',  # Until here
    'Z': 'q',
    'M': 'r',
    'J': 's',
    'P': 't',
    'U': 'u',
    'B': 'v',
    'K': 'w',
    'A': 'x',
    'T': 'y',
    'D': 'z',
}

result = decode(value, translation)
print(result)
# The result making an effort to contain every letter is a hint to the answer lying somewhere in the key

sorted_by_key = sorted(list(translation.items()), key=lambda x: x[0])
print(decode(sorted_by_key[7:13], lambda t: t[1]))

sorted_by_value = sorted(list(translation.items()), key=lambda x: x[1])
print(decode(sorted_by_value[8:16], lambda t: t[0]))
