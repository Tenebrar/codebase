from collections import Counter

from hacker.clustering import cluster
from hacker.decoder import decode

value = '''7A62E92CE518C2CBC5CF5C8B2E7E0A71F4C7D946A8EC64E18C
A32E2CF4A2DEC8D4E0A5637A3A8D2C605E2F7194A3A514D598
B494A7A49710D3B7C592C05B95E4C4D32A9495A3E02E210C36
2B02D38DF81418D08D8CB35C2DA94B41895D8E0A2DCAE7B4D3
E3D32A7F7C69764EF4B8A214102604B4C3C071463C4F7B10C7
D860C981312B7606F5B4F8B05B5F71381B3D4C8C4E86C08C92
64C92D12E8B415B8C5E264C5A3B5C1041102B31A3B04C71071
E01A326F7135B9795A7D892AB3E9818626D31298F494F5B4D5
1B01F2B37E2AF5DF51E3E0814B86E7C8A2D8698C8C2A8AC8B5
17694EE295B34E07C97A0DB012B4A5E9268698A0A2A06517E4
EE046EB3A213C3768A560A717605A7B3BEB2E9713C7B0418D3
C86F7D5F2C04634F2113A04AA0D4A2F2B9792C3C0DF5C07E2E
4A0760D4DB5D35E3C3E5D4F7D010D92E2B26041517A7D0B04A
8E5C8B4637E595A8C4D3A015BF8CB37B38B5CF7D068CAE7B35
1F8E38A4D2C3D0E5A8105E5F8A86010EF7D8B34BE02A0C413A
598CC95D5D5A8F2A0E0EF81468A95F792B41F7EF7D8E5B8F7C
67F7D5CA5F2D0DC0B4E314C4104D7A46512CF5B8F5E95E0C71
8A0E3D7F2D213D4C2C10A8DA0B05A32E7B92A1365B7A8C5C49
56351592D3E2A4B3A312AF292D12E760B0D8B3C0EBAF5D15B0
D2EF5C4B8A312D4D98646F8A717C2604D3C02C51F497F215F8'''

value = value.replace('\n', '')

ALPHABET = '0123456789ABCDEF'
PLAINTEXT_DECREASING = 'xyzw'


def overlapping_substrings(string, size):
    """ Yields all substrings of a given length from a string """
    for i in range(len(string) + 1 - size):
        yield string[i:i+size]

counter = Counter(overlapping_substrings(value, 2))
inputs = {character: tuple([counter[character + character2] for character2 in ALPHABET]) for character in ALPHABET}

# It's no guarantee, but 100 iterations seems to give the same answer consistently
result = cluster(inputs, amount_of_clusters=4, iterations=100)
result = sorted([sorted(character_list) for character_list in result.values()])

expected_result = [['0', '3'], ['1', '6', 'a', 'B', 'c', 'D', 'E'], ['2', '4', '5', '7', '8'], ['9', 'F']]
assert result == expected_result  # Making sure we're not outputting a wrong result if we get unlucky with clustering

counter = Counter(value)
result = sorted(result, key=lambda character_list: -sum([counter[character] for character in character_list]))

translation = {}
for index, character_list in enumerate(result):
    translation.update({character: PLAINTEXT_DECREASING[index] for character in character_list})

result = decode('0123456789ABCDEF', translation)
print(result)
