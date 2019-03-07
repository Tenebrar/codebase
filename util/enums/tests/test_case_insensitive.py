from util.enums.case_insensitive import CaseInsensitiveEnum


class CIEnum(CaseInsensitiveEnum):
    A = 'a'
    B = 'b'


def test_fetch_with_capital():
    assert CIEnum('A') is CIEnum.A


def test_fetch_without_capital():
    assert CIEnum('a') is CIEnum.A
