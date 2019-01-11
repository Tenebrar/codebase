def make_number(number: int) -> str:
    if number < 10:
        return str(number)

    return '52*' + make_number(number // 10) + '*' + str(number % 10) + '+'


def make_char(char: str) -> str:
    return make_number(ord(char))


def write_string(string: str) -> str:
    return ''.join(make_char(char) + 'P' for char in string)
