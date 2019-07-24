from typing import List
from zlib import crc32

from sandbox.fileformats.file_formats import (
    FileFormatException, ListFormat, Variable, BigEndianInt, FixedLengthValue, VariableLengthValue, FixedValue,
    RepeatUntilEof, read_formatted_data
)


class Chunk:
    def __init__(self, chunk_type: str, chunk_data: bytes) -> None:
        self.chunk_type = chunk_type
        self.chunk_data = chunk_data

    def __str__(self) -> str:
        return self.chunk_type

    def __repr__(self) -> str:
        return f'Chunk: {self.chunk_type}'

    def is_critical(self):
        return self.chunk_type[0].isupper()

    def is_ancillary(self):
        return not self.is_critical()


class Png:
    def __init__(self, chunks: List[Chunk]) -> None:
        self.chunks = chunks

    def __str__(self) -> str:
        return str(self.chunks)


class ChunkFactory:
    def __call__(self, chunk_length: int, chunk_type: bytes, chunk_data: bytes, crc: bytes) -> Chunk:
        if crc32(chunk_type + chunk_data) != int.from_bytes(crc, byteorder='big'):
            raise FileFormatException('Incorrect CRC')
        return Chunk(chunk_type.decode(), chunk_data)


class PngFactory():
    def __call__(self, header: bytes, chunks: List[Chunk]) -> Png:
        return Png(chunks)


CHUNK_FORMAT = ListFormat(ChunkFactory(), [
    Variable('chunk length', BigEndianInt()),
    FixedLengthValue(4),
    VariableLengthValue('chunk length'),
    FixedLengthValue(4)
])
PNG_FORMAT = ListFormat(PngFactory(), [
    FixedValue(b'\x89PNG\r\n\x1a\n'),
    RepeatUntilEof(
        CHUNK_FORMAT
    )
])

png = read_formatted_data(PNG_FORMAT, 'C:\\Users\\Peter\\Downloads\\transparent.png')
print(png)
