from hacker.decoder import decode

value = '+90+509+20+355+977+46+685+503+7+98+421+43+45+380+377'

# Source: https://en.wikipedia.org/wiki/List_of_country_calling_codes
translation = {
    '90': 'Turkey',
    '509': 'Haiti',
    '20': 'Egypt',
    '355': 'Albania',
    '977': 'Nepal',
    '46': 'Sweden',
    '685': 'Western Samoa',
    '503': 'El Salvador',
    '7': 'Republic of Kazakhstan',
    '98': 'Iran',
    '421': 'Slovakia',
    '43': 'Austria',
    '45': 'Denmark',
    '380': 'Ukraine',
    '377': 'Monaco',
}

result = decode(value[1:].split('+'), translation, lambda s: s[0])
print(result)
