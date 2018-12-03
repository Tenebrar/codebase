value = '8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba2cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1' # noqa


def decode(ciphertext, key1, key2, forbidden=''):
    """ Does a best effort to decode the ciphertext based on guessing when the encoding made a mistake """
    plaintext = ''
    index = 0
    while index < len(ciphertext):
        decoded = chr(int(ciphertext[index:index+2], 16) ^ key1)
        if decoded.isprintable() and decoded not in forbidden:
            plaintext += decoded
        else:
            plaintext += chr(int(ciphertext[index], 16) ^ key1)
            index -= 1
        key1 = (key1 + key2) % 256
        index += 2

    return plaintext

for i in range(256):
    for j in range(256):
        result = decode(value, i, j)
        if result and result.isprintable() and 'the' in result:
            print(i, j)
            print(result)

# The decoding is not perfect, but good enough to reveal the answer
# We can get the correctly decoded sequence with a few added constraints
print(decode(value, 249, 67, '¨X?'))
