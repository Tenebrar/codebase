from projecteuler.util.divisors import divisor_pairs

# a + b + c = 1000
# a**2 + b**2 = c**2
# It follows:
# a**2 + b**2 = (1000 - b - a)**2
# a**2 + b**2 = 1,000,000 - 1000b - 1000a - 1000b + b**2 + ab - 1000a + ab + a**2
# a**2 + b**2 = 1,000,000 - 2000a - 2000b + 2ab + a**2 + b**2
# 1,000,000 - 2000a - 2000b + 2ab = 0
# 500,000 - 1000a - 1000b + ab = 0
# 1000a - ab = 500,000 - 1000b
# (1000 - b)a = 500,000 - 1000b
# a = (500,000 - 1000b)/(1000 - b)
# a = 1000(-500 + 1000 - b)/(1000 - b)
# a = -500,000/(1000 - b) + 1000
# (1000 - a)(1000 - b) = 500,000


def problem_0009(total: int) -> int:
    for x, y in divisor_pairs(total * total // 2):
        a = total - x
        b = total - y

        c = total - a - b

        if a > 0 and b > 0 and c > 0:
            return a * b * c

    raise ValueError('No solution found')


if __name__ == '__main__':
    SUM = 1000

    print(problem_0009(SUM))
    # Expected: 31875000 (from 200 375 425)
