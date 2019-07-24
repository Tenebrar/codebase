from typing import Tuple

from pytest import mark, param, raises

from util.conditions.exceptions import PreconditionViolatedError
from util.combinatorics.functions import (
    bell_number, binomial_coefficient, catalan_number, combination, combinatorial_number, derangement_number,
    double_factorial, factorial, falling_factorial, hyperfactorial, multinomial_coefficient, odd_factorial,
    polygonal_number, rising_factorial, semi_factorial, stirling_number_of_the_first_kind,
    stirling_number_of_the_second_kind, stirling_set_number, subfactorial
)


@mark.parametrize('value, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 2),
    param(3, 6),
    param(4, 24),
    param(5, 120),
    param(6, 720),
    param(7, 5040),
    param(8, 40320),
    param(9, 362880),
    param(10, 3628800),
    param(20, 2432902008176640000),
))
def test_factorial(value: int, expected: int) -> None:
    assert factorial(value) == expected


@mark.parametrize('value', (
    param(-1),
    param(-10),
    param(-100),
))
def test_factorial_positive(value: int) -> None:
    with raises(PreconditionViolatedError):
        factorial(value)


@mark.parametrize('value, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 2),
    param(3, 3),
    param(4, 8),
    param(5, 15),
    param(6, 48),
    param(7, 105),
    param(8, 384),
    param(9, 945),
    param(10, 3840),
    param(11, 10395),
    param(12, 46080),
    param(13, 135135),
    param(14, 645120),
))
def test_double_factorial(value: int, expected: int) -> None:
    assert double_factorial(value) == expected


@mark.parametrize('value', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_double_factorial_positive(value: int) -> None:
    with raises(PreconditionViolatedError):
        double_factorial(value)


@mark.parametrize('value, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 2),
    param(3, 3),
    param(4, 8),
    param(5, 15),
    param(6, 48),
    param(7, 105),
    param(8, 384),
    param(9, 945),
    param(10, 3840),
    param(11, 10395),
    param(12, 46080),
    param(13, 135135),
    param(14, 645120),
))
def test_semi_factorial(value: int, expected: int) -> None:
    assert semi_factorial(value) == expected


@mark.parametrize('value', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_semi_factorial_positive(value: int) -> None:
    with raises(PreconditionViolatedError):
        semi_factorial(value)


@mark.parametrize('value, expected', (
    param(1, 1),
    param(3, 3),
    param(5, 15),
    param(7, 105),
    param(9, 945),
    param(11, 10395),
    param(13, 135135),
))
def test_odd_factorial(value: int, expected: int) -> None:
    assert odd_factorial(value) == expected


@mark.parametrize('value', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_odd_factorial_positive(value: int) -> None:
    with raises(PreconditionViolatedError):
        odd_factorial(value)


@mark.parametrize('value', (
    param(0),
    param(2),
    param(4),
    param(6),
    param(8),
    param(10),
    param(-2),
    param(-4),
    param(-6),
    param(-8),
    param(-10),
))
def test_odd_factorial_odd(value: int) -> None:
    with raises(PreconditionViolatedError):
        odd_factorial(value)


@mark.parametrize('n, k, expected', (
    param(1, 2, 0),
    param(0, 0, 1),
    param(1, 0, 1),
    param(1, 1, 1),
    param(2, 0, 1),
    param(2, 1, 2),
    param(2, 2, 1),
    param(3, 0, 1),
    param(3, 1, 3),
    param(3, 2, 3),
    param(3, 3, 1),
    param(4, 0, 1),
    param(4, 1, 4),
    param(4, 2, 6),
    param(4, 3, 4),
    param(4, 4, 1),
    param(8, 0, 1),
    param(8, 1, 8),
    param(8, 2, 28),
    param(8, 3, 56),
    param(8, 4, 70),
    param(8, 5, 56),
    param(8, 6, 28),
    param(8, 7, 8),
    param(8, 8, 1),
))
def test_binomial_coefficient(n: int, k: int, expected: int) -> None:
    assert binomial_coefficient(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 2),
    param(1, -2),
    param(-1, -2),
))
def test_binomial_coefficient_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        binomial_coefficient(n, k)


@mark.parametrize('n, k, expected', (
    param(1, 2, 0),
    param(0, 0, 1),
    param(1, 0, 1),
    param(1, 1, 1),
    param(2, 0, 1),
    param(2, 1, 2),
    param(2, 2, 1),
    param(3, 0, 1),
    param(3, 1, 3),
    param(3, 2, 3),
    param(3, 3, 1),
    param(4, 0, 1),
    param(4, 1, 4),
    param(4, 2, 6),
    param(4, 3, 4),
    param(4, 4, 1),
    param(8, 0, 1),
    param(8, 1, 8),
    param(8, 2, 28),
    param(8, 3, 56),
    param(8, 4, 70),
    param(8, 5, 56),
    param(8, 6, 28),
    param(8, 7, 8),
    param(8, 8, 1),
))
def test_combination(n: int, k: int, expected: int) -> None:
    assert combination(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 2),
    param(1, -2),
    param(-1, -2),
))
def test_combination_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        combination(n, k)


@mark.parametrize('n, k, expected', (
    param(1, 2, 0),
    param(0, 0, 1),
    param(1, 0, 1),
    param(1, 1, 1),
    param(2, 0, 1),
    param(2, 1, 2),
    param(2, 2, 1),
    param(3, 0, 1),
    param(3, 1, 3),
    param(3, 2, 3),
    param(3, 3, 1),
    param(4, 0, 1),
    param(4, 1, 4),
    param(4, 2, 6),
    param(4, 3, 4),
    param(4, 4, 1),
    param(8, 0, 1),
    param(8, 1, 8),
    param(8, 2, 28),
    param(8, 3, 56),
    param(8, 4, 70),
    param(8, 5, 56),
    param(8, 6, 28),
    param(8, 7, 8),
    param(8, 8, 1),
))
def test_combinatorial_number(n: int, k: int, expected: int) -> None:
    assert combinatorial_number(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 2),
    param(1, -2),
    param(-1, -2),
))
def test_combinatorial_number_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        combinatorial_number(n, k)


@mark.parametrize('n, k, expected', (
    param(1, 2, 0),
    param(1, 1, 1),
    param(2, 1, 1),
    param(2, 2, 1),
    param(3, 1, 1),
    param(3, 2, 3),
    param(3, 3, 1),
    param(4, 1, 1),
    param(4, 2, 7),
    param(4, 3, 6),
    param(4, 4, 1),
    param(5, 1, 1),
    param(5, 2, 15),
    param(5, 3, 25),
    param(5, 4, 10),
    param(5, 5, 1),
    param(6, 1, 1),
    param(6, 2, 31),
    param(6, 3, 90),
    param(6, 4, 65),
    param(6, 5, 15),
    param(6, 6, 1),
))
def test_stirling_number_of_the_second_kind(n: int, k: int, expected: int) -> None:
    assert stirling_number_of_the_second_kind(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 2),
    param(1, -2),
    param(-1, -2),
))
def test_stirling_number_of_the_second_kind_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        stirling_number_of_the_second_kind(n, k)


@mark.parametrize('n, k, expected', (
    param(1, 2, 0),
    param(1, 1, 1),
    param(2, 1, 1),
    param(2, 2, 1),
    param(3, 1, 1),
    param(3, 2, 3),
    param(3, 3, 1),
    param(4, 1, 1),
    param(4, 2, 7),
    param(4, 3, 6),
    param(4, 4, 1),
    param(5, 1, 1),
    param(5, 2, 15),
    param(5, 3, 25),
    param(5, 4, 10),
    param(5, 5, 1),
    param(6, 1, 1),
    param(6, 2, 31),
    param(6, 3, 90),
    param(6, 4, 65),
    param(6, 5, 15),
    param(6, 6, 1),
))
def test_stirling_set_number(n: int, k: int, expected: int) -> None:
    assert stirling_set_number(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 2),
    param(1, -2),
    param(-1, -2),
))
def test_stirling_set_number_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        stirling_set_number(n, k)


@mark.parametrize('n, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 2),
    param(3, 5),
    param(4, 15),
    param(5, 52),
    param(6, 203),
    param(7, 877),
    param(8, 4140),
    param(9, 21147),
    param(10, 115975),
))
def test_bell_number(n: int, expected: int) -> None:
    assert bell_number(n) == expected


@mark.parametrize('n', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_bell_number_positive(n: int) -> None:
    with raises(PreconditionViolatedError):
        bell_number(n)


@mark.parametrize('n, expected', (
    param(0, 1),
    param(1, 0),
    param(2, 1),
    param(3, 2),
    param(4, 9),
    param(5, 44),
    param(6, 265),
    param(7, 1854),
    param(8, 14833),
))
def test_subfactorial(n: int, expected: int) -> None:
    assert subfactorial(n) == expected


@mark.parametrize('n', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_subfactorial_positive(n: int) -> None:
    with raises(PreconditionViolatedError):
        subfactorial(n)


@mark.parametrize('n, expected', (
    param(0, 1),
    param(1, 0),
    param(2, 1),
    param(3, 2),
    param(4, 9),
    param(5, 44),
    param(6, 265),
    param(7, 1854),
    param(8, 14833),
))
def test_derangement_number(n: int, expected: int) -> None:
    assert derangement_number(n) == expected


@mark.parametrize('n', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_derangement_number_positive(n: int) -> None:
    with raises(PreconditionViolatedError):
        derangement_number(n)


@mark.parametrize('x, n, expected', (
    param(0, 0, 1),
    param(0, 1, 0),
    param(5, 0, 1),
    param(5, 1, 5),
    param(5, 2, 20),
    param(5, 3, 60),
    param(5, 4, 120),
    param(5, 5, 120),
    param(-4, 2, 20),
    param(-4, 3, -120),
))
def test_falling_factorial(x: int, n: int, expected: int) -> None:
    assert falling_factorial(x, n) == expected


@mark.parametrize('x, n', (
    param(0, -1),
    param(5, -2),
    param(10, -10),
))
def test_falling_factorial_positive(x: int, n: int) -> None:
    with raises(PreconditionViolatedError):
        falling_factorial(x, n)


@mark.parametrize('x, n, expected', (
    param(0, 0, 1),
    param(0, 1, 0),
    param(5, 0, 1),
    param(5, 1, 5),
    param(5, 2, 30),
    param(5, 3, 210),
    param(5, 4, 1680),
    param(-4, 2, 12),
    param(-4, 3, -24),
))
def test_rising_factorial(x: int, n: int, expected: int) -> None:
    assert rising_factorial(x, n) == expected


@mark.parametrize('x, n', (
    param(0, -1),
    param(5, -2),
    param(10, -10),
))
def test_rising_factorial_positive(x: int, n: int) -> None:
    with raises(PreconditionViolatedError):
        rising_factorial(x, n)


@mark.parametrize('n, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 4),
    param(3, 108),
    param(4, 27648),
    param(5, 86400000),
    param(6, 4031078400000),
    param(7, 3319766398771200000),
))
def test_hyperfactorial(n: int, expected: int) -> None:
    assert hyperfactorial(n) == expected


@mark.parametrize('n', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_hyperfactorial_positive(n: int) -> None:
    with raises(PreconditionViolatedError):
        hyperfactorial(n)


@mark.parametrize('n, expected', (
    param((0,), 1),
    param((1, 2, 4), 105),
    param((1, 2, 4, 4), 34650),
))
def test_multinomial_coefficient(n: Tuple[int, ...], expected: int) -> None:
    assert multinomial_coefficient(*n) == expected


@mark.parametrize('n', (
    param((-1,)),
    param((-1, 2)),
    param((1, -2)),
    param((-1, -2)),
    param((-1, 2, 3)),
    param((1, -2, 3)),
    param((1, 2, -3)),
))
def test_multinomial_coefficient_positive(n: Tuple[int, ...]) -> None:
    with raises(PreconditionViolatedError):
        multinomial_coefficient(*n)


@mark.parametrize('n, expected', (
    param(0, 1),
    param(1, 1),
    param(2, 2),
    param(3, 5),
    param(4, 14),
    param(5, 42),
    param(6, 132),
    param(7, 429),
    param(8, 1430),
    param(9, 4862),
    param(10, 16796),
))
def test_catalan_number(n: int, expected: int) -> None:
    assert catalan_number(n) == expected


@mark.parametrize('n', (
    param(-1),
    param(-2),
    param(-10),
    param(-11),
    param(-100),
    param(-101),
))
def test_catalan_number_positive(n: int) -> None:
    with raises(PreconditionViolatedError):
        catalan_number(n)


@mark.parametrize('sides, n, expected', (
    param(3, 1, 1),
    param(3, 2, 3),
    param(3, 3, 6),
    param(3, 4, 10),
    param(4, 1, 1),
    param(4, 2, 4),
    param(4, 3, 9),
    param(4, 4, 16),
    param(5, 1, 1),
    param(5, 2, 5),
    param(5, 3, 12),
    param(5, 4, 22),
    param(6, 1, 1),
    param(6, 2, 6),
    param(6, 3, 15),
    param(6, 4, 28),
))
def test_polygonal_number(sides: int, n: int, expected: int) -> None:
    assert polygonal_number(sides, n) == expected


@mark.parametrize('sides, n', (
    param(-1, 1),
    param(0, 1),
    param(1, 1),
    param(2, 1),
))
def test_polygonal_number_at_least_three(sides: int, n: int) -> None:
    with raises(PreconditionViolatedError):
        polygonal_number(sides, n)


@mark.parametrize('sides, n', (
    param(3, 0),
    param(3, -1),
    param(3, -2),
    param(4, 0),
    param(4, -1),
    param(4, -2),
))
def test_polygonal_number_strict_positive(sides: int, n: int) -> None:
    with raises(PreconditionViolatedError):
        polygonal_number(sides, n)


@mark.parametrize('n, k, expected', (
    param(1, 1, 1),
    param(2, 1, -1),
    param(2, 2, 1),
    param(3, 1, 2),
    param(3, 2, -3),
    param(3, 3, 1),
    param(4, 1, -6),
    param(4, 2, 11),
    param(4, 3, -6),
    param(4, 4, 1),
    param(5, 1, 24),
    param(5, 2, -50),
    param(5, 3, 35),
    param(5, 4, -10),
    param(5, 5, 1),
))
def test_stirling_number_of_the_first_kind(n: int, k: int, expected: int) -> None:
    assert stirling_number_of_the_first_kind(n, k) == expected


@mark.parametrize('n, k', (
    param(-1, 1),
    param(-2, 2),
    param(1, -1),
    param(2, -2),
))
def test_stirling_number_of_the_first_kind_positive(n: int, k: int) -> None:
    with raises(PreconditionViolatedError):
        stirling_number_of_the_first_kind(n, k)
