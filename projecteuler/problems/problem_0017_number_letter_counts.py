NUMBERS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

RULES = [(100, 'hundred'), (1000, 'thousand'), (1000000, 'million')]
RULES = sorted(RULES, reverse=True)


def write_number(number: int) -> str:
    """ Returns the written out version of a number in English """
    try:
        return NUMBERS[number]
    except KeyError:
        if number < 100:
            return f'{write_number(number // 10 * 10)} {write_number(number % 10)}'

        for rule in RULES:
            if number >= rule[0]:
                multiplier = number // rule[0]
                remainder = number % rule[0]
                if remainder:
                    return f'{write_number(multiplier)} {rule[1]} and {write_number(remainder)}'
                return f'{write_number(multiplier)} {rule[1]}'

        raise ValueError(f'Could not handle: {number}')


def problem_0017(maximum: int) -> int:
    return sum(len(write_number(i).replace(' ', '')) for i in range(1, maximum + 1))


if __name__ == '__main__':
    MAXIMUM = 1000  # If going over 1 billion, add to the RULES list

    print(problem_0017(MAXIMUM))
    # Expected: 21124
