from functools import partial
from typing import Callable, Dict, Tuple

from hacker.bytestreams import substrings

value = '#FF0000,#00FF00,#0000FF'

# Simple conversion from hex values to colors in RGB spectrum
# Apparently CSS 2.1 defines #00ff00 as 'lime' instead, but 'green' is the expected answer
COLOR_NAMES: Dict[Tuple[int, ...], str] = {
    (255, 0, 0): 'red',
    (0, 255, 0): 'green',
    (0, 0, 255): 'blue',
}

base16: Callable[[str], int] = partial(int, base=16)
base16.__doc__ = 'Convert a hexadecimal string to an int'


def hex_str_to_color_name(val: str) -> str:
    tup: Tuple[int, ...] = tuple(map(base16, substrings(val[1:], 2)))
    return COLOR_NAMES[tup]


print(','.join(map(hex_str_to_color_name, value.split(','))))
