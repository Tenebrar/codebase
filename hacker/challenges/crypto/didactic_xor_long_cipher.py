from hacker.bytestreams import bytes_from_hex, skip, offset
from hacker.decoder import transform

value = '8776459cf37d459fbb7b5ecfbb7f5fcfb23e478aaa3e4389f378439aa13e4e96a77b5fc1f358439df36a4486a03e4381b63e5580a66c0c8ebd6d5b8aa13e459cf34e4d9fa67f02cf90714288a17f589abf7f5886bc705fcfbc700c96bc6b5ecfb7775f8cbc68499daa3f'  # noqa


def is_acceptable(c):
    """ Returns whether a given character is considered potentially in the result string """
    return 'a' <= c.lower() <= 'z' or c in ' .?!\'",'


def get_key_options(key_index, ciphertext):
    """ Returns only the potential keys that map ALL the characters it would be used for to an acceptable one """
    for key_option in range(256):
        bytes_for_key = skip(offset(bytes_from_hex(ciphertext), key_index), 4)
        if all(transform(bytes_for_key, lambda byte: byte ^ key_option, chr, is_acceptable)):
            yield key_option

key_space = [get_key_options(j, value) for j in range(4)]

for key1 in key_space[0]:
    for key2 in key_space[1]:
        for key3 in key_space[2]:
            for key4 in key_space[3]:
                key = [key1, key2, key3, key4]
                result = ''
                for index, b in enumerate(bytes_from_hex(value)):
                    result += chr(b ^ key[index % 4])

                print(result)
