from util.enums.defaulting import DefaultingEnum


class DEnum(DefaultingEnum):
    A = 'a'
    B = 'b'

    UNKNOWN = 'unknown'


def test_fetch_by_name():
    assert DEnum('a') == DEnum.A


def test_fetch_incorrect_name():
    assert DEnum('c') == DEnum.UNKNOWN
