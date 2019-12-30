from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict, Any, List, Callable

from sandbox.fileformats.file_utils import ByteStreamReader, read_file


class FormatException(Exception):
    """ Exception indicating the read data is not the expected format. """


X = TypeVar('X', covariant=True)


class DataFormat(ABC, Generic[X]):
    """ Object that can read data and interpret it to make an instance of X """

    @abstractmethod
    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> X:
        """
        Read data from a ByteStreamReader and return an instance of X

        :param data: A ByteStreamReader
        :param parameters: A dict to hold parameters (starts empty, allows for communication between child formats)
        :return: An instance of X
        :raises FormatException: if the data does not adhere to the right format
        """


Y = TypeVar('Y')


def read_formatted_data(data: bytes, data_format: DataFormat[Y]) -> Y:
    """
    Reads byte data with a certain format

    :param data: Bytes that form the data to be read
    :param data_format: A DataFormat
    :return: An instance of Y
    :raises FormatException: if the data does not adhere to the right format
    """
    stream = ByteStreamReader(data)
    return data_format.read(stream, {})


class FixedLengthValue(DataFormat[bytes]):
    def __init__(self, length: int) -> None:
        self.length = length

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> bytes:
        return data.read(self.length)


class BigEndianInt(DataFormat[int]):
    def __init__(self, number_of_bytes=4):
        self.number_of_bytes = number_of_bytes

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> int:
        return int.from_bytes(data.read(self.number_of_bytes), byteorder='big')


Z = TypeVar('Z')


class Variable(DataFormat[Z]):
    def __init__(self, variable_name: str, file_format: DataFormat[Z]) -> None:
        self.variable_name = variable_name
        self.file_format = file_format

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> Z:
        result = self.file_format.read(data, parameters)
        parameters[self.variable_name] = result
        return result


class VariableLengthValue(DataFormat[bytes]):
    def __init__(self, variable_name: str) -> None:
        self.variable_name = variable_name

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> bytes:
        return data.read(parameters[self.variable_name])


class FixedValue(DataFormat[bytes]):
    def __init__(self, value: bytes) -> None:
        self.value = value

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> bytes:
        result = data.read(len(self.value))
        if result != self.value:
            raise FormatException('Expected {self.value}, but got {result}')
        return result


A = TypeVar('A')


class RepeatUntilEof(DataFormat[List[A]]):
    def __init__(self, child_format: DataFormat[A]):
        self.child_format = child_format

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> List[A]:
        result = []
        while not data.depleted():
            result.append(self.child_format.read(data, parameters))
        return result


B = TypeVar('B')


class ListFormat(DataFormat[B]):
    def __init__(self, factory: Callable[..., B], child_format_list: List[DataFormat[Any]]) -> None:
        self.factory = factory
        self.child_format_list = child_format_list

    def read(self, data: ByteStreamReader, parameters: Dict[str, Any]) -> B:
        values = [child_format.read(data, parameters) for child_format in self.child_format_list]
        return self.factory(*values)
