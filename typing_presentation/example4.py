from typing import List


def find(strings: List[str]) -> str:
    # What is wrong with this function?
    for string in strings:
        if len(string) > 5:
            return string
