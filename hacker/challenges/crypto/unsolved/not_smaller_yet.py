from collections import Counter

value = '(34)e.rugressgsdtedsme  . -prr wierohrhdmhelht ssnnatTWgTtks hoe rriiaacolfwffyrseoTtoaooruiiawnnu x  t eoB   oe '  # noqa

print(len(value))  # 113 prime, when removing '(34)' we get 109 which is also prime

print(Counter(value))

for i, c in enumerate(value):
    if c.isupper():
        print(i, c)


def get_forward_distances(char1, char2):
    results = []
    for i1, c1 in enumerate(value):
        if c1 == char1:
            for i2, c2 in enumerate(value):
                if c2 == char2:
                    results.append( (i2 - i1) % (len(value)) )
    return sorted(set(results))

a = get_forward_distances('t', 'h')
b = get_forward_distances('h', 'e')
c = get_forward_distances('e', ' ')

print(sorted(a))
print(sorted(b))
print(sorted(c))
print(sorted([x for x in a if x in b and x in c]))


for i, c in enumerate(value):
    if c == 'T':
        index = i
        for _ in range(100):
            print(value[index], end='')
            index += 34
            if index >= len(value):
                index -= (len(value))
        print()
