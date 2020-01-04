from itertools import combinations

from advent_of_code.util import input_file

with input_file() as file:
    labels = [line.rstrip('\n') for line in file]


def diff(label1, label2):
    count = 0
    for i in range(len(label1)):
        if label1[i] != label2[i]:
            count += 1
    return count


def merge(label1, label2):
    result = ''
    for i in range(len(label1)):
        if label1[i] == label2[i]:
            result += label1[i]
    return result


for label1, label2 in combinations(labels, 2):
    if diff(label1, label2) == 1:
        print(merge(label1, label2))
        break