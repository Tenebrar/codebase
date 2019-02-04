# extract the gz file, then
# Write the data in HEX for get calls
# tcpdump -A -r smellassweet > smellassweetgets

from hacker.settings import inputfile

for line in open(inputfile('web', 'smell_as_sweet', 'smellassweetgets')):
    if line.startswith('\t0x'):
        t = line[10:].strip().replace(' ', '')
        for i in range(0, len(t), 2):
            print(chr(int(t[i:i + 2], 16)), end='')
        print()
