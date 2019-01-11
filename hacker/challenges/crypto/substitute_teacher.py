from hacker.decoder import decode

value = 'ISS NVVK DIPXYWA PIT AVSUY QIAOP PWZEHVNWIEDZ. CDYT ZVM LOTK HDY AVSMHOVT HV HDOA HYFH, ZVM COSS QY IQSY HV NYH HDY ITACYW, CDOPD OA IKMGQWIHY.'  # noqa

translation = {
    'I': 'a',
    'T': 'n',
    'a': 's',
    'c': 'w',
    'Y': 'e',
    'W': 'r',
    'S': 'l',
    'H': 't',
    'D': 'h',
    'O': 'i',
    'V': 'o',
    'N': 'g',
    'Q': 'b',
    'K': 'd',
    'P': 'c',
    'X': 'k',
    'U': 'v',
    'Z': 'y',
    'E': 'p',
    'M': 'u',
    'L': 'f',
    'F': 'x',
    'G': 'm',
}

result = decode(value, translation)
print(result)
