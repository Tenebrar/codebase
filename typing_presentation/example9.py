from typing import Callable, Dict, Type

from typing_presentation.classes import Cat, Mammal


def fun(m: Cat) -> None:
    print(m)


ANIMAL_MAPPING: Dict[Type[Mammal], Callable[[Mammal], None]] = {
    Cat: fun,
}
