from typing import List, cast
from zlib import crc32

from sandbox.fileformats.file_formats import (
    BigEndianInt, FixedLengthValue, FixedValue, FormatException, ListFormat, RepeatUntilEof, Variable,
    VariableLengthValue, read_formatted_data
)
from sandbox.fileformats.file_utils import read_file
from sandbox.fileformats.subclass_registration import SubclassRegister


class Chunk(SubclassRegister, key='chunk_type'):
    @classmethod
    def create(cls, chunk_type: bytes, chunk_data: bytes, crc: bytes) -> 'Chunk':
        if crc32(chunk_type + chunk_data) != int.from_bytes(crc, byteorder='big'):
            raise FormatException('Incorrect CRC')

        # This is technically incorrect, since arbitrary bytes might be used which do not map on a character
        chunk_type = chunk_type.decode()

        try:
            return cls.get_subclass(chunk_type)(chunk_data)
        except KeyError:
            # If it is not a known chunk
            chunk = Chunk(chunk_type, chunk_data)

            if chunk.is_critical():
                raise FormatException(f'Unknown critical chunk {chunk.chunk_type}')

            print(f'Unknown, but non-critical chunk: {chunk.chunk_type}')

            return chunk

    def __init__(self, chunk_type: str, chunk_data: bytes) -> None:
        if chunk_type[2].islower():
            raise FormatException('Illegal chunk type. Second letter must be capitalized.')

        self.chunk_type = chunk_type
        self.chunk_data = chunk_data

    def verify_correctness(self, chunks: List['Chunk']):
        pass  # A base Chunk has nothing to check

    def __str__(self) -> str:
        return self.chunk_type

    def __repr__(self) -> str:
        return f'Chunk: {self.chunk_type}'

    def is_critical(self):
        return self.chunk_type[0].isupper()

    def is_ancillary(self):
        return not self.is_critical()

    def is_public(self):
        return self.chunk_type[1].isupper()

    def is_private(self):
        return not self.is_public()

    def is_only_copiable_if_critical_chunks_unchanged(self):
        return self.chunk_type[3].isupper()

    def is_always_copiable(self):
        return not self.is_only_copiable_if_critical_chunks_unchanged()


class Png:
    def __init__(self, chunks: List[Chunk]) -> None:
        if len(chunks) < 3:
            raise FormatException('At least 3 chunks are required in a png image (IHDR, IDAT, IEND).')

        for chunk in chunks:  # Allow the chunks to do checks on other chunks for correctness
            chunk.verify_correctness(chunks)

        self.chunks = chunks

    def __str__(self) -> str:
        return str(self.chunks)


CHUNK_FORMAT = ListFormat(lambda length, chunk_type, chunk_data, crc: Chunk.create(chunk_type, chunk_data, crc), [
    Variable('chunk length', BigEndianInt()),
    FixedLengthValue(4),
    VariableLengthValue('chunk length'),
    FixedLengthValue(4)
])
PNG_FORMAT = ListFormat(lambda header, chunks: Png(chunks), [
    FixedValue(b'\x89PNG\r\n\x1a\n'),
    RepeatUntilEof(
        CHUNK_FORMAT
    )
])


class IhdrChunk(Chunk):
    chunk_type = 'IHDR'

    format = ListFormat(lambda *args: args, [BigEndianInt(), BigEndianInt(), BigEndianInt(1), BigEndianInt(1),
                                             BigEndianInt(1), BigEndianInt(1), BigEndianInt(1)])

    def __init__(self, chunk_data: bytes) -> None:
        super().__init__(IhdrChunk.chunk_type, chunk_data)

        self.width, self.height, self.bit_depth, self.color_type, self.compression_method, self.filter_method, \
            self.interlace_method = read_formatted_data(chunk_data, IhdrChunk.format)

        if not 0 < self.width <= pow(2, 31):
            raise FormatException('Width must be in range ]0, 2**31]')
        if not 0 < self.height <= pow(2, 31):
            raise FormatException('Width must be in range ]0, 2**31]')
        if self.bit_depth not in [1, 2, 4, 8, 16]:
            raise FormatException('Bit depth must be in [1, 2, 4, 8, 16]')
        if self.color_type not in [0, 2, 3, 4, 6]:
            raise FormatException('Color type must be in [0, 2, 3, 4, 6]')
        if self.compression_method not in [0]:
            raise FormatException('Compression method must be in [0]')
        if self.filter_method not in [0]:
            raise FormatException('Filter method must be in [0]')
        if self.interlace_method not in [0, 1]:
            raise FormatException('Interlace method must be in [0, 1]')

        allowed_bit_depths = {
            0: [1, 2, 4, 8, 16],
            2: [8, 16],
            3: [1, 2, 4, 8],
            4: [8, 16],
            6: [8, 16],
        }
        if self.bit_depth not in allowed_bit_depths[self.color_type]:
            raise FormatException('Bit depth does not match color type.')

        self.sample_depth = self.bit_depth if self.color_type != 3 else 8

    def verify_correctness(self, chunks: List['Chunk']):
        # The first chunk must be and only the first chunk may be an IHDR chunk
        if chunks[0].chunk_type != 'IHDR':
            raise FormatException('First chunk must be IHDR chunk.')
        if any(chunk.chunk_type == 'IHDR' for chunk in chunks[1:]):
            raise FormatException('Only first chunk may be IHDR chunk.')

        # color type 3 (indexed color) must have a PLTE chunk
        if self.color_type == 3:
            if not any(chunk.chunk_type == 'PLTE' for chunk in chunks):
                raise FormatException('PLTE chunk is required for indexed color image.')
        # color types 0 and 4 (grayscale and grayscale with alpha) may not have a PLTE chunk
        if self.color_type in [0, 4]:
            if any(chunk.chunk_type == 'PLTE' for chunk in chunks):
                raise FormatException('PLTE chunk is not allowed for grayscale image.')


class IdatChunk(Chunk):
    chunk_type = 'IDAT'

    def __init__(self, chunk_data: bytes) -> None:
        super().__init__(IdatChunk.chunk_type, chunk_data)

    def verify_correctness(self, chunks: List['Chunk']):
        # TODO There can be multiple IDAT chunks; if so, they must appear consecutively with no other intervening chunks
        pass


class PlteChunk(Chunk):
    chunk_type = 'PLTE'

    format = RepeatUntilEof(ListFormat(lambda *args: args, [BigEndianInt(1), BigEndianInt(1), BigEndianInt(1)]))

    def __init__(self, chunk_data: bytes) -> None:
        super().__init__(PlteChunk.chunk_type, chunk_data)

        self.values = read_formatted_data(chunk_data, PlteChunk.format)

    def verify_correctness(self, chunks: List['Chunk']):
        if sum(1 for c in chunks if c.chunk_type == PlteChunk.chunk_type) > 1:
            raise FormatException('There must not be more than one PLTE chunk.')

        for c in chunks:
            if c.chunk_type == PlteChunk.chunk_type:
                break
            if c.chunk_type == IdatChunk.chunk_type:
                raise FormatException('If this chunk does appear, it must precede the first IDAT chunk.')

        if len(self.values) > pow(2, cast(IhdrChunk, chunks[0]).bit_depth):
            raise FormatException('Too many palette entries')


class IendChunk(Chunk):
    chunk_type = 'IEND'

    def __init__(self, chunk_data: bytes) -> None:
        super().__init__(IendChunk.chunk_type, chunk_data)

        if chunk_data:
            raise FormatException('IEND chunk should be empty.')

    def verify_correctness(self, chunks: List['Chunk']):
        # The last chunk must be and only the last chunk may be an IEND chunk
        if chunks[-1].chunk_type != 'IEND':
            raise FormatException('Last chunk must be IEND chunk.')
        if any(chunk.chunk_type == 'IEND' for chunk in chunks[:-1]):
            raise FormatException('Only last chunk may be IEND chunk.')


#png = read_formatted_data(read_file('/Users/peter/Downloads/chart.png'), PNG_FORMAT)
png = read_formatted_data(read_file('/Users/peter/Downloads/transparent.png'), PNG_FORMAT)
print(png)
