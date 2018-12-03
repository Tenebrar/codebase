from hacker.bytestreams import substrings
from hacker.codes import BRAILLE
from hacker.decoder import decode

value = [
    ' . .  .     .  ..  .  . .  .      .  .     . .  .  .. .. .  ..  .  . .  .  .. .. .  ',
    '.. ..  .        . .  ..  . ..    .  .     .   .     .  .  . .  .  .  .   .  .     . ',
    '.              .  .   .    .        .     .  .  .. .     .     .     .     .        ',
]

result = decode(zip(substrings(value[0], 3), substrings(value[1], 3), substrings(value[2], 3)),
                lambda t: t[0][0:2] + t[1][0:2] + t[2][0:2],
                BRAILLE)
print(result)
