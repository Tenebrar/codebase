import numpy as np

value = '''4T4 2Z2 8S5 3V2 1L4 9W8 0M3 7N2 6G7 1X3
0L1 1W7 5U3 5D3 7H2 5N9 4I8 8E2 1Z5 8R0
5A7 8N4 1I4 0Y5 7E3 1S1 1H8 7V2 0D1 3L0
6O5 9I0 8A6 0R4 3S6 3O4 1V4 8J3 0I0 0A0
7J4 0S0 4O8 8N0 6H1 8Q6 2A9 6G3 4F2 1S3
0I7 7G2 2H4 9B3 8M4 9I3 9C2 4X4 6T2 8S8
7I0 3E2 9G4 5V2 2I0 7N0 3X1 5I9 8B2 9W1
9I3 1B4 6G0 8S4 6T0 0Y0 0W2 3S0 4H3 0T9
7D2 5E0 6R7 2K5 4S6 1A3 2N5 6D5 5T2 5R3
2T4 0X5 3B2 3K8 9S3 8H5 3U7 0M4 2S7 9A9'''


array = np.array(value.split()).reshape((10, 10))

result = ''
row, col = 0, 0
while True:
    s = array[row][col]
    result += s[1]
    row, col = int(s[0]), int(s[2])

    if (row, col) == (0, 0):
        break

print(result)
