from projecteuler.problems.problems_0051_0100.problem_0051_prime_digit_replacements import problem_0051
from projecteuler.problems.problems_0051_0100.problem_0052_permuted_multiples import problem_0052
from projecteuler.problems.problems_0051_0100.problem_0053_combinatoric_selections import problem_0053


def test_problem_0051():
    assert problem_0051(6) == 13
    assert problem_0051(7) == 56003
    assert problem_0051(8) == 121313


def test_problem_0052():
    assert problem_0052() == 142857


def test_problem_0053():
    assert problem_0053() == 4075
