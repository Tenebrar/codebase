from collections import Counter
import re


def index_of_coincidence(value, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Returns the index of coincidence for a given ciphertext string (a value used to determin whether a poly-alphabetic
    cipher was used or not)
    :param value: A ciphertext string
    :param alphabet: The letters to be taken into account for the index
    :return: The index of coincidence of the string
    """
    value = value.upper()
    value = re.sub(f'[^{alphabet}]', '', value)
    counter = Counter(value)

    n = len(value)

    index = 0
    for c in alphabet:
        ni = counter[c]
        index += (ni * (ni - 1)) / (n * (n - 1))

    return index

# Ciphertexts with indexes close to regular english are probably simple substitution ciphers
# Lower indexes indicate polyalphabetic ciphers (with Vigenere around 0.04)
ENGLISH_INDEX_OF_COINCIDENCE = 0.0667
