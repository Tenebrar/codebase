from projecteuler.problems.problems_0051_0100.problem_0051_prime_digit_replacements import problem_0051
from projecteuler.problems.problems_0051_0100.problem_0052_permuted_multiples import problem_0052
from projecteuler.problems.problems_0051_0100.problem_0053_combinatoric_selections import problem_0053
from projecteuler.problems.problems_0051_0100.problem_0054_poker_hands import problem_0054
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


def test_problem_0063():
    assert problem_0063() == 49
