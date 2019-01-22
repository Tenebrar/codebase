from re import compile

from hacker.settings import inputfile

filename = inputfile('web', 'lorem_ipsum', 'lorem.txt')

with open(filename, 'r') as file:
    value = file.read().lower()

words = compile('\w+').findall(value)

words.sort()

for i in range(1, len(words) - 1):
    if words[i - 1] != words[i] and words[i] != words[i + 1]:
        print(words[i])
        break
