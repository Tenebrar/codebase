# If you could run this python program, what would it print?
# def D(n): return n and (2*n-1)*D(n-1) or 1
# def N(n): return n and (4*n*n-8*n+3)*N(n-2)+7*D(n-2) or 1
# b=1000000000000; print (N(b*4)*b)/D(b*4)


def D(n):
    # https://oeis.org/A001147 Double factorial of odd numbers
    # 1, 1, 3, 15, 105, 945, 10395, 135135, 2027025, 34459425, 654729075, 13749310575, 316234143225, 7905853580625, 213458046676875, 6190283353629375, 191898783962510625, 6332659870762850625, 221643095476699771875, 8200794532637891559375  # noqa
    res = 1
    for i in range(1, 2 * n, 2):
        res *= i
    return res


def D2(n):
    if n == 0:
        return 1

    return (2 * n - 1) * D(n - 1)


def N(n):
    if n == 0:
        return 1
    return (2 * n - 3) * (2 * n - 1) * N(n - 2) + 7 * D(n - 2)


def N2(n):
    if n == 0:
        return 1
    return (2 * n - 3) * (2 * n - 1) * N(n - 2) + 7 * D(n - 2)


def N_over_D(n):
    return N(n) / D(n)


def N_over_D2(n):
    if n == 0:
        return 1
    # This is still exactly the same, later changes cause rounding errors
    # return ((2 * n - 3) * (2 * n - 1) * N(n - 2) + 7 * D(n - 2)) / ((2 * n - 3) * (2 * n - 1) * D(n - 2))

    # return N_over_D(n - 2) + 7 / ((2 * n - 3) * (2 * n - 1))

    res = 0
    for i in range(1, n + 1,  2):
        res += 1 / (4 * i * i - 1)

    return res * 7 + 1


for i in range(0, 20, 2):
    n, n2 = N(i), N2(i)
    print(n == n2, n, n2)

print()

for i in range(0, 20, 2):
    d, d2 = D(i), D2(i)
    print(d == d2, d, d2)

print()

from math import isclose
for i in range(0, 20, 2):
    nd, nd2 = N_over_D(i), N_over_D2(i)
    print(isclose(nd, nd2, rel_tol=0, abs_tol=10e-12), nd, nd2)


# print(N_over_D2(4 * 1000000000000) * 1000000000000)