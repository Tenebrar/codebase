# More info: https://mypy.readthedocs.io/en/latest/generics.html#variance-of-generic-types
from abc import abstractmethod, ABC
from typing import Generic, TypeVar, Optional

from typing_presentation.classes import Mammal, Cat, Animal

ConverterInputType = TypeVar('ConverterInputType', contravariant=True)
ConverterOutputType = TypeVar('ConverterOutputType', covariant=True)


class Converter(ABC, Generic[ConverterInputType, ConverterOutputType]):
    """Converts an input value to a value of a different type."""
    @abstractmethod
    def __call__(self, input_value: ConverterInputType) -> ConverterOutputType:
        """
        Converts an input value to a value of a different type
        :param input_value: the input value
        :return: the converted value
        :raises ConversionException: when the data is incorrect for conversion
        :raises ObjectNotFoundException: when the converted data does not match an expected object in our backend
        """


def my_function(converter: Converter[Mammal, Mammal]) -> None:
    converter(Cat())


# Which of these Converters can be passed to the function?
c: Converter
# c: Converter[Optional[Mammal], Mammal] = None
# c: Converter[Animal, Mammal] = None
# c: Converter[Cat, Mammal] = None
# c: Converter[Mammal, Cat] = None
# c: Converter[Mammal, Optional[Mammal]] = None

my_function(c)
