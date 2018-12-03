from hacker.decoder import decode

translation = {
    'B': ' ',
    'x': 'T',
    'q': 'H',
    'f': 'E',
    't': 'W',
    'o': 'I',
    'z': 'C',
    'r': 'O',
    'w': 'F',
    'p': 'N',
    'j': 'Y',
    'y': 'B',
    'a': 'L',
    'g': 'R',
    'v': 'A',
    'l': 'M',
    'd': 'S',
    'h': 'V',
    'i': 'U',
    'n': 'P',
    'k': 'G',
    's': 'K',
    'u': 'Z',
    'c': 'X',
    'e': 'J',

    'm': '.',

    'A': 'D'  # to make the ciphertext all in lowercase
}

value = 'xqfBprtAodflyrAofABhozxoldBdriadBtqozqBqiyyvgABzvaafABxqfxvpdBtfgfByartpBopxrBxqfBvogByjBxqfByavdxmBxqfjBtfgfBzvnxigfAByjBcfpidBwrgzfdBidopkBvpBfafzxgrpozBgoyyrpBvpABdizsfABopxrBhvziilBurpfdBvgripABxqfBtrgaAmBxqfBqipAgfAdBrwByoaaorpdBrwBzvnxigfABxqfxvpdBtfgfBxvsfpBxrBvBxjnfBrwBzopflvBtqfgfBxqfjBtfgfBwrgzfABxrBtvxzqBvBxqgffABdinfgBzrarddvaBlrxorpBnozxigfBwrgBxqogxjdocBAvjdmBxqodBolnavpxfABtqvxBqiyyvgABxfglfABhvgoridBlodafvAopkBAvxvBopxrBxqfBlflrgofdBrwBxqfBqvnafddBxqfxvpdBtqozqBqvdBxrBArBtoxqBkrABxqfBAfhoaBdnvzfBrnfgvBfxBzfxfgvmBxqodBopzaiAfABvaaBtrgaABgfaokorpdBtoxqBqiyyvgABdnfzowozvaajBvxxgoyixopkBgrlvpBzvxqraozodlBvpABxqfBolvkfBrwBxqfBzgizowocorpBxrBxqfBopwaifpzfBrwBcfpimBxqfBxtrBolnavpxBdxvxorpdBzoxfAByjBqiyyvgABtfgfBdvoABxrBqvhfByffpBarzvxfABrpBqvtvooBvpABavdBnvalvdBopBxqfBzvpvgjBodavpAdmBopBvAAoxorpBxrBolnavpxopkBpftByfaofwdBopBxqfBxqfxvpdBxqfBolvkfdBAfngohfABxqflBrwBxqfogBdfpdfBrwBnfgdrpvaBoAfpxoxjmBtqfpBxqfBxqfxvpdBafwxBxqfBngrefzxorpBvgfvdBxqfjBdxvgxfABxrBzaidxfgBxrkfxqfgBopBkgrindBrwBvBwftBxqridvpABqvhopkBardxBxqfBvyoaoxjBxrBAowwfgfpxovxfByfxtffpBfvzqBrxqfgmBfvzqBzaidxfgBrwBxqfxvpdBkvxqfgfABopxrBrpfBrwBxqfBwftBgflvopopkByrAofdBxqvxBdighohfABxqfBfcnardorpmBxqfdfByfzvlfBtqvxBvgfBsprtpBvdByrAjBxqfxvpdBtqozqBvgfBdvoABxrByfBdxoaaBzaopkopkBxrBvpABvAhfgdfajBvwwfzxopkBfhfgjrpfBfczfnxBxqrdfBdzofpxrarkodxdBtqrBqvhfBnfgwrglfABxqfBpfzfddvgjBdxfndBxrBgflrhfBxqflm'  # noqa

result = decode(value, translation)
print(result)

print(result[:10])
