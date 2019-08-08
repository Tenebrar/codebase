from contextlib import contextmanager
from inspect import stack
from os import path


@contextmanager
def input_file():
    calling_frame = stack()[2]  # Needs to be 1 higher than "normal" because of the contextmanager decorator
    calling_filename = calling_frame[0].f_code.co_filename
    calling_directory = path.dirname(calling_filename)

    util_directory = path.dirname(__file__)

    relative_path = path.relpath(calling_directory, util_directory)
    filename = path.join('C:\\Users\\Peter\\Documents\\advent_of_code', relative_path, 'input.txt')

    with open(filename) as file:
        yield file
