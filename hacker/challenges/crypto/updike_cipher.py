from hacker.settings import inputfile

filename = inputfile('crypto', 'updike_cipher', 'updike.html')

result = ''
with open(filename, 'r') as file:
    previous_line = ''
    for line in file.readlines():
        if previous_line.startswith('<p>'):
            result += line[0] if line[0].isalpha() else ''
        previous_line = line

print(result)