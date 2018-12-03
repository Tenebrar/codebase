from hacker.decoder import decode
from hacker.settings import inputfile

value = 'Thy raiment waxed not old upon thee, neither did thy foot swell, these forty years. And it shall be, when the officers have made an end of speaking unto the people that they shall make captains of the armies to lead the people. And it shall be, if thou have no delight in her, then thou shalt let her go whither she will; but thou shalt not sell her at all for money, thou shalt not make merchandise of her, because thou hast humbled her. Look down from thy holy habitation, from heaven, and bless thy people Israel, and the land which thou hast given us, as thou swarest unto our fathers, a land that floweth with milk and honey. Now therefore write ye this song for you, and teach it the children of Israel: put it in their mouths, that this song may be a witness for me against the children of Israel. But Jeshurun waxed fat, and kicked: thou art waxen fat, thou art grown thick, thou art covered with fatness; then he forsook God which made him, and lightly esteemed the Rock of his salvation. And I commanded you at that time all the things which ye should do. When a man hath taken a new wife, he shall not go out to war, neither shall he be charged with any business: but he shall be free at home one year, and shall cheer up his wife which he hath taken. When a man hath taken a wife, and married her, and it come to pass that she find no favour in his eyes, because he hath found some uncleanness in her: then let him write her a bill of divorcement, and give it in her hand, and send her out of his house. They shall call the people unto the mountain; there they shall offer sacrifices of righteousness: for they shall suck of the abundance of the seas, and of treasures hid in the sand. Cursed shalt thou be when thou comest in, and cursed shalt thou be when thou goest out.'  # noqa

filename = inputfile('crypto', 'didactic_text_2', 'bible.txt')


def find_bible_verse(verse):
    """
    Find the specific bible verse in a file containing the King James edition of the bible (Source: gutenberg.org)
    """
    with open(filename, 'r') as file:
        for line in file.readlines():
            if verse[:50] in line:  # The text file has extra newlines, so only check the start for matching
                return line.split()[0]


def index_to_letter(index):
    """ Convert a 1-index to a letter in the alphabet: 1 -> a,... """
    return chr(ord('a') + index - 1)

result = decode(value.split('. '), find_bible_verse, lambda s: int(s.split(':')[1]), index_to_letter)
print(result)
