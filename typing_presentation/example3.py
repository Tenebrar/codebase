from typing_presentation.classes import *


def fun(mammal: Mammal) -> None:
    print(mammal)


# Which of these calls is ok?
# fun(Cat())
# fun(Mammal())
# fun(Animal())
# fun(Bird())
# fun(Peacock())
