from hacker.bytestreams import substrings
from hacker.decoder import decode

value = 'TACTGTGTGCTCATTCGGTTATCGACCCTTTCCACTTAATCAATCCCCTCTCTTCTCTTGACT'

# DNA to RNA translation
dna_to_rna = {'t': 'A', 'a': 'U', 'c': 'G', 'g': 'C'}
value = decode(value.lower(), dna_to_rna)

# RNA codon to protein translation
# Source: https://en.wikipedia.org/wiki/Genetic_code
translation = {
    'UUU': 'F',    'UCU': 'S',    'UAU': 'Y',    'UGU': 'C',
    'UUC': 'F',    'UCC': 'S',    'UAC': 'Y',    'UGC': 'C',
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
    'GUU': 'V',    'GCU': 'A',    'GAU': 'D',    'GGU': 'G',
    'GUC': 'V',    'GCC': 'A',    'GAC': 'D',    'GGC': 'G',
    'GUA': 'V',    'GCA': 'A',    'GAA': 'E',    'GGA': 'G',
    'GUG': 'V',    'GCG': 'A',    'GAG': 'E',    'GGG': 'G',
}

assert value[0:3] == 'AUG'  # The initiation site for encoding

result = decode(substrings(value[3:], 3), translation)
print(result)
