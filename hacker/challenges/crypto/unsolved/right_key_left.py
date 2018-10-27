import numpy as np

value = '''1T3 4C1 2O6 4Y7 2E1 3I6 3G2
4T6 3H5 1P3 2I6 3D4 1O5 5C2
5D7 6X1 2T4 7Y4 4G5 4R3 2G1
2Y5 5R1 1M2 3X1 5R6 5X1 4E2
5Y2 3W1 8W1 1L6 2I5 4F2 3U7
6W7 1P9 2W1 2T3 3R2 1P5 7J6
2U6 2O5 2V1 1P2 1J7 4U7 1J5'''

temp = ''
for s in value.split():
    temp += s[1]

from collections import Counter

ctr = Counter(temp)

print(ctr)


array = np.array(value.split()).reshape((7, 7))

result = ''
row, col = 0, 0
for _ in range(100):
    s = array[row][col]
    result += s[1]
    row = (row + int(s[0])) % 7
    col = (col + int(s[2])) % 7

    if (row, col) == (0, 0):
        break

print(result)
