def s2(n, k):
    """
    Returns the Stirling number of the second kind

    :param n: The number of  items (distinguishable)
    :param k: The number of boxes (indistinguishable)
    :return: The number of ways to partition a set of n labelled objects into k nonempty unlabelled subsets
    """
    result = 0
    for j in range(k + 1):
        result += (-1)**(k-j) * comb(k, j) * (j**n)

    result /= fac(k)
    return result


def fac(k):
    """
    Returns the factorial of the number

    :param k: The number of items
    :return: The number of permutations for those items
    """
    result = 1
    for i in range(1, k + 1):
        result *= i
    return result


def comb(n, k):
    """
    Returns the combination number

    :param n: The number of items
    :param k: The number of selected items
    :return: The number of ways to select k items from n options
    """
    return fac(n) / (fac(n-k) * fac(k))
