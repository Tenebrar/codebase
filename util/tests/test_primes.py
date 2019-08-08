from pytest import mark, param

from util.primes import is_prime, is_probable_prime, extract_power_of_two, get_probable_prime


@mark.parametrize('value, expected', (
    param(-4, False),
    param(-3, False),
    param(-2, False),
    param(-1, False),
    param(0, False),
    param(1, False),
    param(2, True),
    param(3, True),
    param(4, False),
    param(5, True),
    param(6, False),
    param(7, True),
    param(8, False),
    param(9, False),
    param(10, False),
    param(11, True),
    param(12, False),
    param(13, True),
    param(14, False),
    param(15, False),
    param(16, False),
    param(17, True),
    param(18, False),
    param(19, True),
    param(20, False),
))
def test_is_prime(value: int, expected: bool) -> None:
    assert is_prime(value) == expected


@mark.parametrize('value, expected', (
    param(0, False),
    param(1, False),
    param(2, True),
    param(3, True),
    param(982451651, False),
    param(982451652, False),
    param(982451653, True),
))
def test_is_probable_prime(value: int, expected: bool) -> None:
    assert is_probable_prime(value) == expected


@mark.parametrize('value, power, odd', (
    param(220, 2, 55),
    param(264, 3, 33),
    param(263, 0, 263),
))
def test_extract_power_of_two(value: int, power: int, odd: int) -> None:
    assert extract_power_of_two(value) == (power, odd)


@mark.parametrize('num_bits', (
    param(3),
    param(33),
    param(333),
))
def test_get_probable_prime(num_bits: int) -> None:
    prime = get_probable_prime(num_bits)
    assert prime < 2 ** num_bits
    assert is_probable_prime(prime)
