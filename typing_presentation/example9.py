from typing import Callable, Dict, Type

from typing_presentation.classes import Cat, Dog, Mammal


def cat_fun(m: Cat) -> None:
    print(m)


def dog_fun(m: Dog) -> None:
    print(m)


def mammal_fun(m: Mammal) -> None:
    print(m)


ANIMAL_MAPPING: Dict[Type[Mammal], Callable[[Mammal], None]] = {
    Cat: cat_fun,
    Dog: mammal_fun,
    Mammal: mammal_fun,
}
