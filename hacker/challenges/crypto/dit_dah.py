from hacker.codes import MORSE
from hacker.decoder import decode

value = '- .... . .- -. ... .-- . .-. .. ... .... --- .- .-. ... .'

result = decode(value.split(), MORSE)
print(result)
