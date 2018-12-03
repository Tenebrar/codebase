import re
import numpy as np

from hacker.cryptanalysis import index_of_coincidence

value = "Uvgz ckzzff uhs qxuf hfvuirl vbzyecusczc, iuv xgx tyslu dg uvc toud tbggj ctihuolhlacat. W yt swbw uvya yqe, so oqwitsfh cp wetrsqg yjcqwhmwqoef rsdycy, wkvd iotl nq djpizse dbwbygug vrw fbayyrdapb. Uoep igv rm, fow gamz iuoy dzbh Khdcqstqyy iu dzf olzwgb lior dinv tswln yqe lp hfl nghl mstll. Vrat qgwhgb at ylvwp kk uvc ciiofffc, hnf sk iilkrgnk pt wlatc gmr. Ga iu ostwjf avdsdyck tjbgvuf mrgamfbaf apkdzggz. Iu dzbh fvw aym bdnyocmzfr ga? I'o wslwln a psuf zmug kxhvh rlxv sf pfblr vy hsctpdg tmth cuowqz eorh fqb qpip hncvqtwq. Ahg Ofhzgzh nkfhiyne ysdm pcarci lis nsakxlflr ahtymhv gas qgf qoraetxk."  # noqa
# key = 'BOYHACKS'

print(f'index of coincidence: {index_of_coincidence(value)}; indicative of Vigenere cipher')


def kasiski_test(ciphertext, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """ Use Kasiski test to find the keylength of a Vigenere encrypted ciphertext """
    # Source: https://en.wikipedia.org/wiki/Kasiski_examination (Superposition)
    ciphertext = ciphertext.upper()
    ciphertext = re.sub(f'[^{alphabet}]', '', ciphertext)

    return max(range(2, 10), key = lambda shift:
               len([i for i in range(0, len(ciphertext) - shift) if ciphertext[i] == ciphertext[i + shift]]))

# Source: https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
# Frequency table for the English language as a numpy array with the frequency of the letter 'A' at index 0 and so on.
# The sum is not exactly 1, presumably through rounding errors
ENGLISH_FREQUENCIES = np.array([0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
                                0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                                0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
                                0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                                0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074])


def calculate_frequency_table(ciphertext):
    """
    Calculate a frequency table for a string. Returns a numpy array with the frequency of the letter 'A' at index 0
    and so on.
    :param ciphertext: A string only containing uppercase characters
    :return: A frequency table as a numpy array
    """
    frequency_table = np.zeros(26)
    for c in ciphertext:
        frequency_table[ord(c) - ord('A')] += 1
    frequency_table /= len(ciphertext)
    return frequency_table


def decrypt_vigenere(ciphertext, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """ Decrypt a ciphertext encoded with a Vigenere cipher """
    original_value = ciphertext
    # Make uppercase and remove punctuation for more easy analysis
    ciphertext = re.sub(f'[^{alphabet}]', '', ciphertext.upper())

    key_length = kasiski_test(ciphertext)
    print(f'Kasiski test suggests key length: {key_length}')

    full_key = ''
    for i in range(key_length):
        frequency_table = calculate_frequency_table(ciphertext[i::key_length])

        # We take as key the letter whose shifted frequency table most closely matches that of English
        key = min(range(26), key = lambda c : sum((np.roll(frequency_table, -c) - ENGLISH_FREQUENCIES) ** 2))

        full_key += chr(ord('A') + key)

    print(f'The suspected key is {full_key}')

    return decode_vigenere(original_value, full_key)


def decode_vigenere(ciphertext, key):
    """
    Decode a ciphertext encoded with the Vigenere cipher and the given key. The ciphertext may contain punctuation,
    it will remain unchanged
    """
    plaintext = ''
    index = 0
    for c in ciphertext:
        if not c.isalpha():
            plaintext += c
        else:
            plaintext += decode_vigenere_character(c, key[index % len(key)])
            index += 1

    return plaintext


def decode_vigenere_character(character, key):
    """
    Decode a single character according to the Vigenere cipher.
    Will maintain the case of the ciphertext character
    """
    a_value = ord('a') if character.islower() else ord('A')
    return chr((ord(character.lower()) - ord(key.lower())) % 26 + a_value)

result = decrypt_vigenere(value)
print(result)
