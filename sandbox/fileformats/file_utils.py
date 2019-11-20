from util.conditions.decorators import multi_value_precondition, precondition
from util.conditions.predicates import is_positive


def read_file(filename: str) -> bytes:
    """
    Opens a file, reads its contents as bytes, and returns it.

    :param filename: A filename
    :return: The bytes in the file
    :raises IOError: upon failure
    """
    with open(filename, 'rb') as file:
        return file.read()


class ByteStreamReader:
    """ Class that handles a bytes object like a stream of bytes """
    def __init__(self, data: bytes) -> None:
        """
        :param data: a bytes object
        """
        self.data = data
        self.index = 0

    def depleted(self) -> bool:
        """ Returns whether there is no more data available. """
        return self.available() == 0

    def available(self) -> int:
        """ Returns the amount of bytes still available """
        return len(self.data) - self.index

    @precondition('amount', is_positive)
    def read(self, amount: int) -> bytes:
        """
        Returns the next 'amount' of bytes

        :param amount: a positive integer
        :return: the next 'amount' bytes in the data
        :raises PreconditionViolatedError: if amount is negative
        :raises IndexError: if not enough bytes are available
        """
        self.seek(self.index + amount)
        return self.data[self.index - amount:self.index]

    def reset(self) -> None:
        """ Resets the stream to the beginning. """
        self.seek(0)

    @multi_value_precondition(['self', 'index'], lambda self, index: 0 <= index <= len(self.data),
                              lambda d: IndexError(
                                  f"Index {d['index']} is out of bounds of for data of length {len(d['self'].data)}."))
    def seek(self, index: int) -> None:
        """
        Sets the stream to a given position.

        :param index: A positive integer in the range [0, len(bytes)]
        :raises IndexError: If the given position is not a valid position in the stream
        """
        self.index = index
