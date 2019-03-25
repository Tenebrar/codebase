from typing_presentation.classes import Mammal


def fun(mammal: Mammal) -> None:
    print(mammal)


# Which of these calls is ok?
# function(Cat())
# function(Mammal())
# function(Animal())
# function(Bird())
# function(Peacock())
