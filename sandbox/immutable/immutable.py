from types import MappingProxyType

# Dicts
m = {'a': 1, 'b': 2}
test = MappingProxyType({'a': 1, 'b': 2})

print(test['a'])

for k, v in test.items():
    print(k, v)

print(m.get('c'))
print(test.get('c'))

# Sets
s2 = {1, 2, 3}
s2.add(4)
print(s2)

s = frozenset([1, 2, 3])

print(s)

s.add(4)
