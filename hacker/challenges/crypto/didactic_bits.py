from hacker.bytestreams import bytes_from_binary
from hacker.decoder import decode

value = 'abbbabaaabbabaaaabbaababaabaaaaaabbaaaababbabbbaabbbaabbabbbabbbabbaabababbbaabaaabaaaaaabbabaababbbaabbaabaaaaaabbaaaababbaabaaabbbabababbabbababbaaabaabbbaabaabbaaaababbbabaaabbaabab'  # noqa

translation = {'a': '0', 'b': '1'}
value = decode(value, translation)

result = decode(bytes_from_binary(value), chr)
print(result)
