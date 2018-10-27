# Converted from the given code
def hacker_test_it(x):
    return (x & (x - 1)) == 0

for i in range(20):
    print(i, hacker_test_it(i))

# Only in a power of two are all bits changed by subtracting one
print('power of two')
