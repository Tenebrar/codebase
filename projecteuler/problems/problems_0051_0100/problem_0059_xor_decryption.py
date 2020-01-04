from collections import Counter
from itertools import cycle
from typing import Tuple

from projecteuler.settings import inputfile
from projecteuler.util.timing import print_time


def _decode(ciphertext: str, key: str) -> str:
    """ Decodes a string given a key. Also can be used for encoding, as the process is the same with XOR encryption """
    return ''.join(chr(ord(value) ^ ord(k)) for value, k in zip(ciphertext, cycle(key)))


def _decrypt(input: str, key_length: int) -> Tuple[str, str]:
    """ This will do a really simple decrypt based on the assumption that ' ' is the most occurring character """
    key = ''
    for i in range(key_length):
        counter = Counter(input[i::key_length])
        key += chr(ord(counter.most_common()[0][0]) ^ ord(' '))

    return key, _decode(input, key)

def problem_0059(filename: str) -> int:
    with open(inputfile(filename), 'r') as file:
        values = ''.join(chr(int(i)) for i in file.read().split(','))

    _, decrypted = _decrypt(values, 3)

    return sum(map(ord, decrypted))


if __name__ == '__main__':
    FILENAME = 'p059_cipher.txt'

    print(problem_0059(FILENAME))
    # Expected: 129448
