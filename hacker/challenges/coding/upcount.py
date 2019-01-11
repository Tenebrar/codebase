value = 11589


# Converted from java, gives: "RecursionError: maximum recursion depth exceeded in comparison"
def calc(depth):
    if depth == 0:
        return 1
    cc = calc(depth - 1)
    return cc + (depth % 7) + (1 if (((cc ^ depth) % 4) == 0) else 0)


# Converted original recursive function into iterative function
def recalc(depth):
    cc = 1
    for i in range(1, depth + 1):
        cc = cc + (i % 7) + (1 if (((cc ^ i) % 4) == 0) else 0)
    return cc


for i in range(10, 20):
    assert calc(i) == recalc(i)

print(recalc(value))
