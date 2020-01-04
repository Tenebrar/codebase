from string import ascii_lowercase

from advent_of_code.util import input_file

with input_file() as file:
    polymer = file.read().rstrip('\n')


def matches(char1: str, char2: str) -> bool:
    return char1 != char2 and char1.lower() == char2.lower()


def react(polymer, ignore: str):
    stack = ['.']
    for c in polymer:
        if c == ignore or c.lower() == ignore:
            pass
        elif matches(c, stack[-1]):
            stack.pop()
        else:
            stack.append(c)
    stack.pop(0)
    return len(stack)


char = min(ascii_lowercase, key=lambda x: react(polymer, x))
print(char, react(polymer, char))
