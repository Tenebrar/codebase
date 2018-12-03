from hacker.decoder import decode, int16

value = '5a 63 08 47 16 08 07 35 10 4b 6e 0a 59 13 44 10'

# periodical table, atomic weights to abbreviations of elements
# Source: https://nl.wikipedia.org/wiki/Periodiek_systeem
translation = {
    90: 'Th',
    99: 'Es',
    8: 'O',
    71: 'Lu',
    22: 'Ti',
    7: 'N',
    53: 'I',
    16: 'S',
    75: 'Re',
    110: 'Ds',
    10: 'Ne',
    89: 'Ac',
    19: 'K',
    68: 'Er',
}

result = decode(value.split(), int16, translation)
print(result)
