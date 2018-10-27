from hacker.decoder import decode

translation = {
    'B': ' ',
    'C': 'G',
    'h': 'I',
    'e': 'S',
    'j': 'H',
    'm': 'M',
    't': 'T',
    'x': 'W',
    'p': 'E',
    'u': 'O',
    'q': 'Y',
    'l': 'D',
    'g': 'A',
    'v': 'B',
    'b': 'F',
    'd': 'R',
    's': 'N',
    'c': 'L',
    'f': 'C',
    'z': 'U',
    'k': 'K',
    'o': 'P',
    'a': 'V',
}

value = 'tulgqBmqBvuqbdhpslBtuclBmpBjpBfuzclstBjgsCBuztBxhtjBmpBvpfgzepBjpBbpctBdpgccqBehfk.BhBxpstBtuBjheBjuzepBgsqxgqBtuBezdodhepBjhmBxhtjBjumpmglpBeuzo.BhBxgckBhsBtuBjheBduumBuscqBtuBbhslBjhmBjuukhsCBzoBxhtjBmqBehetpd.BejpBfgstBldhap.BuzdBmumBlduapBjpdBtjpdp.Bbmc'  # noqa

result = decode(value, translation)
print(result)

print(result[:25])
