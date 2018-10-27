from hacker.decoder import decode, int16

value = '79 65 73 79 65 73 79 65 73 79 65 73 79 65 73 79 0d 0a 65 73 79 65 73 79 65 73 79 65 73 79 65 73 79 65 0d 0a 73 79 45 73 79 65 53 79 65 73 59 45 53 79 65 73 0d 0a 79 65 53 59 65 73 59 65 73 59 65 73 79 45 73 79 0d 0a 65 73 59 45 73 79 45 73 79 45 73 79 65 53 79 65 0d 0a 73 79 45 73 59 65 53 79 65 53 79 65 73 59 65 73 0d 0a 79 65 53 79 45 73 59 65 73 59 65 73 79 45 73 79 0d 0a 65 73 59 65 73 59 45 73 79 45 73 79 65 53 79 65 0d 0a 73 79 45 73 79 45 53 79 65 53 79 65 73 59 65 73 0d 0a 79 65 53 79 65 73 59 65 73 79 45 53 59 65 73 79 0d 0a 65 73 79 65 73 79 65 73 79 65 73 79 65 73 79 65 0d 0a 73 79 65 73 79 65 73 79 65 73 79 65 73 79 65 73 0d 0a'  # noqa


def translate(c):
    """ Turn upper case characters into a visible character, lower case into invisible. Maintain newlines """
    if c == '\n':
        return c
    return 'X' if c.isupper() else ' '

result = decode(value.split(), int16, chr, translate)

print(result)