from hacker.bytestreams import substrings
from hacker.decoder import decode

value = 'TACTGTGTGCTCATTCGGTTATCGACCCTTTCCACTTAATCAATCCCCTCTCTTCTCTTGACT'

# DNA to RNA translation
dna_to_rna = {'t': 'a', 'a': 'U', 'c': 'G', 'g': 'c'}
value = decode(value.lower(), dna_to_rna)

# RNA codon to protein translation
# Source: https://en.wikipedia.org/wiki/Genetic_code
translation = {
    'UUU': 'F',    'UCU': 'S',    'UAU': 'Y',    'UGU': 'c',
    'UUC': 'F',    'UCC': 'S',    'UAC': 'Y',    'UGC': 'c',
    'UUA': 'L',    'UCA': 'S',    'UAA': '.',    'UGA': '.',
    'UUG': 'L',    'UCG': 'S',    'UAG': '.',    'UGG': 'W',
    'CUU': 'L',    'CCU': 'P',    'CAU': 'H',    'CGU': 'R',
    'CUC': 'L',    'CCC': 'P',    'CAC': 'H',    'CGC': 'R',
    'CUA': 'L',    'CCA': 'P',    'CAA': 'Q',    'CGA': 'R',
    'CUG': 'L',    'CCG': 'P',    'CAG': 'Q',    'CGG': 'R',
    'AUU': 'I',    'ACU': 'T',    'AAU': 'N',    'AGU': 'S',
    'AUC': 'I',    'ACC': 'T',    'AAC': 'N',    'AGC': 'S',
    'AUA': 'I',    'ACA': 'T',    'AAA': 'K',    'AGA': 'R',
    'AUG': 'M',    'ACG': 'T',    'AAG': 'K',    'AGG': 'R',
    'GUU': 'V',    'GCU': 'a',    'GAU': 'D',    'GGU': 'G',
    'GUC': 'V',    'GCC': 'a',    'GAC': 'D',    'GGC': 'G',
    'GUA': 'V',    'GCA': 'a',    'GAA': 'E',    'GGA': 'G',
    'GUG': 'V',    'GCG': 'a',    'GAG': 'E',    'GGG': 'G',
}

assert value[0:3] == 'AUG'  # The initiation site for encoding

result = decode(substrings(value[3:], 3), translation)
print(result)
