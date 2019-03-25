from typing import List

from typing_presentation.classes import Animal, Cat, Mammal


def my_func(l: List[Mammal]) -> None:
    print(l)


# Types are inferred automatically
lia = [Animal(), Animal()]
lib = [Mammal(), Mammal()]
lic = [Cat(), Cat()]

# With which lists can I call the function?
# my_func(lia)
# my_func(lib)
# my_func(lic)
