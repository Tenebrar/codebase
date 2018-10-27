from hacker.decoder import decode

# Since this is basically just another substitution cipher, I used a letter for each figure
value = 'ABCDEAFGDCDHIFJKLDAFMCNOIBCAKMPQ'

# This is the dancing men cipher, from sherlock holmes. Men holding flags indicate the end of the word, but otherwise
# the same letter. The key can be found with google
translation = {
    'A': 'a',
    'B': 's ',
    'C': 'w',
    'D': 'e ',
    'E': 'd',
    'F': 'n',
    'G': 'c',
    'M': 's',
    'N': 'e',
    'O': 'r ',
    'K': 't',
    'L': 'h',
    'I': 'i',
    'H': 'f',
    'J': 'd ',
    'P': 'o',
    'Q': 'n ',
}

result = decode(value, translation)
print(result)
