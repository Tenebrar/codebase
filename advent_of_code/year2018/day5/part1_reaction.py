from advent_of_code.util import input_file

with input_file() as file:
    polymer = file.read().rstrip('\n')


def matches(char1: str, char2: str) -> bool:
    return char1 != char2 and char1.lower() == char2.lower()


stack = ['.']
for c in polymer:
    if matches(c, stack[-1]):
        stack.pop()
    else:
        stack.append(c)
stack.pop(0)

print(stack)
print(len(stack))
