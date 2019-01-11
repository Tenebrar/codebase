from hacker.settings import inputfile

filename = inputfile('coding', 'pi_hates_nines', 'pi1000000.txt')

with open(filename, 'r') as file:
    pi = file.read().strip()

result = sorted(list(pi.split('9')), key=len)[-1]

print(result)