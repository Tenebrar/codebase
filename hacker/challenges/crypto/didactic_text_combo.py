from hacker.decoder import decode

value = 'in cryptography, a substitution cipher is a method of encryption by which units of plainteXt are suBstituted with ciphertext according to a regular system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. the receiver deciphers the text by performinG an inverse substitution. substitution ciphers can be compared with tRansposition ciphers. in a transposition cipher, the units of the plaintext are rearranged in a different and usually quite complex order, but the units themselves are left unchanged. by contrast, in a substitution cipher, the units of the plaintext are retained in the same sequence in the ciphertext, but the units themselves are altered. there are a number of different types of substitution cipher. if the cipher operates on single letters, it is termed a simple substitution cipher; a cipher that operates on larger groups of letters is termed polygraphic. a monoalphabetic cipher uses fixed substitution over the entire message, Whereas a polyalphabetic cipher uses a number of substItutions at different times in the message such as with homophones, where a unit from the plaintext is mapped to one of several possibilities in the Ciphertext. substitution over a sinGle letter simple substitution can be Demonstrated by writing out the alphabet in some order to represent the substitution. this is termed a substitution alphabet. the cipher alphabet may be shifted or reversed (creating the caesar and atbash ciphers, respectively) or scrambled in a more complex fashion, in which case it is called a mixed alphabet or deranged alphabet. traditionally, mixed alphabets are created by first writing out a keyword, removing repeated letters in it, then writing all the remaining letters in the alphabet. a disadvantage of this method of derangement is that the last letters of the alphabet (which are mostly low freQuency) tend to stay at the end. a stronger way of constructIng a mixed alphabet is to perform a columnar transposition on the ordinary alphabet using the keyword, but this is not often done. although the number of possible keys is very large (26! = 288.4, or about 88 bits), this Cipher is not very strong, beinG easily broken. provided the message is of reasonable length (see below), the cryptanalyst can deduce the probable meaning of the most common symbols by analyzing the frequency distRibution of the cipherteXt frequency analysis. this allows formation of partial words, which can be tentatively filled in, progressively expanding the (partial) solution (see frequency analysis for a demonstration of this). in some cases, underlying words can also Be determined from the pattern of their letters; for example, attract, osseous, and words with those two as the root are the only common enGlish words with the pattern abbcaDb. many people soLve such ciphers for recReation, as With cryptogram puzzles in the newspaper. accordinG to the unicity distance of english, 27.'  # noqa

translation = {
    'X': 't',
    'B': 'h',
    'G': 'e',
    'R': 'a',
    'W': 'n',
    'I': 's',
    'C': 'w',
    'D': 'r',
    'Q': 'i',
    'L': 'v',
}

result = decode(filter(str.isupper, value), translation)
print(result)
