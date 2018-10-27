from hacker.bytestreams import substrings
from hacker.decoder import decode

value = 'fmpmfpmpp mmmpppfmmfppmpppff fmpppf pmfmffmpfmpp, fmpmfpmpp fmfpppmfffpmmpppfffmmmpp, mmmpppmpm mppfpmmpppffffmfmpmfpmffpppmfm mfffmm mpfppfpfffmpffmfmpfppppf'  # noqa

# To make decoding easier, we also make the puntuation take 3 characters
temp = decode(value, {' ': '   ', ',': ',,,'})

translation = {
    '   ': ' ',
    ',,,': ',',

    'fmp': 'T',
    'mfp': 'H',
    'mpp': 'E',
    'ppf': 'O',
    'mmm': 'A',
    'ppp': 'N',
    'fmm': 'S',
    'fpp': 'W',
    'pff': 'R',
    'mpm': 'D',
    'fmf': 'U',
    'pmf': 'L',
    'mff': 'I',
    'mpf': 'F',
    'fpm': 'V',
    'ffm': 'Y',
    'mfm': 'G',
}

result = decode(substrings(temp, 3), translation)
print(result)
