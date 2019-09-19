from contextlib import contextmanager
from datetime import datetime


@contextmanager
def print_time():
    time = datetime.now()
    yield
    print(f'Took {datetime.now() - time}')
