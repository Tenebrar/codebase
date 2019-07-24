from util.conditions.decorators import precondition
from util.conditions.predicates import is_greater_than_or_equal, each, is_odd, is_positive, is_strict_positive


@precondition(0, is_positive)
def factorial(k: int) -> int:
    """
    Returns the factorial of the number, the product of all positive integers smaller or equal to the number.
    By convention an empty product is considered 1, meaning factorial(0) will return 1.

    :param k: A positive integer
    :return: The factorial of that integer
    """
    result = 1
    for i in range(1, k + 1):
        result *= i
    return result


@precondition(0, is_positive)
def double_factorial(k: int) -> int:
    """
    Returns the double factorial of the number, the product of all positive integers of the same parity smaller or
    equal to the number.
    By convention an empty product is considered 1, meaning double_factorial(0) will return 1.

    :param k: A positive integer
    :return: The double factorial of that integer
    """
    result = 1
    for i in range(1 if k % 2 == 1 else 2, k + 1, 2):
        result *= i
    return result


semi_factorial = double_factorial  # synonym


@precondition(0, is_odd)
def odd_factorial(k: int) -> int:
    """ This is nearly a synonym for the double_factorial, but it is only defined for odd numbers """
    return double_factorial(k)


@precondition([0, 1], is_positive)
def binomial_coefficient(n: int, k: int) -> int:
    """
    Returns the binomial coefficient

    Defined as: factorial(n) // (factorial(n - k) * factorial(k))

    :param n: The number of items
    :param k: The number of selected items
    :return: The number of ways to select k items from n options
    """
    if k > n:
        return 0
    k = min(k, n - k)  # take advantage of symmetry
    c = 1
    for i in range(k):
        c = (c * (n - i)) // (i + 1)
    return c


combination = binomial_coefficient
combinatorial_number = binomial_coefficient


@precondition([0, 1], is_positive)
def stirling_number_of_the_second_kind(n: int, k: int) -> int:
    """
    Returns the Stirling number of the second kind

    :param n: The number of  items (distinguishable)
    :param k: The number of boxes (indistinguishable)
    :return: The number of ways to partition a set of n labelled objects into k nonempty unlabelled subsets
    """
    result = 0
    for j in range(k + 1):
        result += (-1) ** (k-j) * binomial_coefficient(k, j) * (j ** n)

    result //= factorial(k)
    return result


stirling_set_number = stirling_number_of_the_second_kind


@precondition(0, is_positive)
def bell_number(n: int) -> int:
    """
    Returns the Bell number

    :param n: A number of items
    :return: The number of ways to partition a set into nonempty subsets
    """
    result = 0
    for k in range(n + 1):
        result += stirling_number_of_the_second_kind(n, k)
    return result


@precondition(0, is_positive)
def subfactorial(n: int) -> int:
    """
    Returns the subfactorial, the number of permutations of n objects in which no object appears in its natural place
    (i.e., "derangements").

    :param n: A positive integer
    :return: The subfactorial of that integer
    """
    if n == 0:
        return 1

    fac_n = factorial(n)
    result = 0
    for k in range(n + 1):
        result += fac_n * (-1)**(n - k) // factorial(n - k)

    return result


derangement_number = subfactorial


@precondition('n', is_positive)
def falling_factorial(x: int, n: int) -> int:
    """
    Returns the falling factorial of the given number to the given depth.
    x(x-1)...(x-(n-1))

    :param x: The number to take the falling factorial of
    :param n: The depth to which to take the falling factorial
    :return: The falling factorial of the given number to the given depth
    """
    result = 1
    for i in range(n):
        result *= x - i

    return result


@precondition('n', is_positive)
def rising_factorial(x: int, n: int) -> int:
    """
    Returns the rising factorial of the given number to the given height.
    x(x+1)...(x+(n-1))

    :param x: The number to take the rising factorial of
    :param n: The height to which to take the rising factorial
    :return: The rising factorial of the given number to the given height
    """
    result = 1
    for i in range(n):
        result *= x + i

    return result


@precondition(0, is_positive)
def hyperfactorial(k: int) -> int:
    """
    Returns the hyperfactorial of the number, the product of all positive integers to the power of themselves smaller
    or equal to the number.
    By convention an empty product is considered 1, meaning hyperfactorial(0) will return 1.

    :param k: A positive integer
    :return: The hyperfactorial of that integer
    """
    result = 1
    for i in range(1, k + 1):
        result *= i**i
    return result


@precondition(0, each(is_positive))
def multinomial_coefficient(*args: int) -> int:
    """
    Returns the multinomial coefficient, the factorial of the sum divided by each of the factorials.

    :param args: positive integers
    :return: The multinomial coefficient for these integers
    """
    result = factorial(sum(args))
    for a in args:
        result //= factorial(a)
    return result


@precondition(0, is_positive)
def catalan_number(k: int) -> int:
    """
    Returns the catalan number of an integer

    :param k: A positive integer
    :return: The catalan number of that integer
    """
    return binomial_coefficient(2*k, k) // (k + 1)


@precondition(0, is_greater_than_or_equal(3))
@precondition(1, is_strict_positive)
def polygonal_number(sides: int, n: int) -> int:
    """
    Returns the n-th polygonal number for a given number of sides.
    A polygonal number is a number represented as dots or pebbles arranged in the shape of a regular polygon.

    :param sides: The number of sides of the polygon
    :param n: A positive number
    :return: The n-th polygonal number for a given number of sides
    """
    return (sides - 2)*n*(n-1)//2 + n


@precondition([0, 1], is_positive)
def stirling_number_of_the_first_kind(n: int, k: int) -> int:
    """
    Returns one of the coefficients s(n, k) in the expansion of the falling factorial

    s(3,3)=1, s(3,2)=-3, s(3,1)=2, because x(x-1)(x-2) = 1x^3 - 3x^2 + 2x

    :param n: The depth of the falling factorial
    :param k: The coefficient in the expansion
    :return: The desired coefficient s(n, k) in the expansion of the falling factorial
    """
    if n == k:
        return 1
    if k == 0 or k > n:
        return 0
    return -(n - 1) * stirling_number_of_the_first_kind(n - 1, k) + stirling_number_of_the_first_kind(n - 1, k - 1)
