from projecteuler.problems.problems_0051_0100.problem_0051_prime_digit_replacements import problem_0051
from projecteuler.problems.problems_0051_0100.problem_0052_permuted_multiples import problem_0052
from projecteuler.problems.problems_0051_0100.problem_0053_combinatoric_selections import problem_0053
from projecteuler.problems.problems_0051_0100.problem_0054_poker_hands import problem_0054
from projecteuler.problems.problems_0051_0100.problem_0055_lychrel_numbers import problem_0055
from projecteuler.problems.problems_0051_0100.problem_0056_powerful_digit_sum import problem_0056
from projecteuler.problems.problems_0051_0100.problem_0057_square_root_convergents import problem_0057
from projecteuler.problems.problems_0051_0100.problem_0058_spiral_primes import problem_0058
from projecteuler.problems.problems_0051_0100.problem_0059_xor_decryption import problem_0059
from projecteuler.problems.problems_0051_0100.problem_0063_powerful_digit_counts import problem_0063


def test_problem_0051():
    assert problem_0051(6) == 13
    assert problem_0051(7) == 56003
    assert problem_0051(8) == 121313


def test_problem_0052():
    assert problem_0052() == 142857


def test_problem_0053():
    assert problem_0053() == 4075


def test_problem_0054():
    assert problem_0054('p054_poker.txt') == 376


def test_problem_0055():
    assert problem_0055(10000) == 249


def test_problem_0056():
    assert problem_0056(100) == 972


def test_problem_0057():
    assert problem_0057(1000) == 153


def test_problem_0058():
    assert problem_0058(0.1) == 26241


def test_problem_0059():
    assert problem_0059('p059_cipher.txt') == 129448


def test_problem_0063():
    assert problem_0063() == 49
