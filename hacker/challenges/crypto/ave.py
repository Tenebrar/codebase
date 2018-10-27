from hacker.ciphers import rot
from hacker.decoder import decode

value = 'cqrb lryqna rb fjh, fjh qjamna cqjw axc cqracnnw. qnan, hxd wnena twxf qxf oja cx bqroc! xq kh cqn fjh, cqn jwbfna rb mnjmvjwblqnbc.'  # noqa

# Simply try all the keys
for key in range(26):
    result = decode(value, lambda x: rot(x, key))

    if 'the' in result:
        break

print(result)
