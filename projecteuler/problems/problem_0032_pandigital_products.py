def _is_pandigital_product(multiplicand: int, multiplier: int) -> bool:
    product = multiplicand * multiplier

    return sorted(f'{multiplicand}{multiplier}{product}') == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def problem_0032() -> int:
    # The ranges are set based on reasoning based on the amount of digits
    results = set()
    # The smalles multiplicand cannot have more than 2 digits (the product would not fit otherwise)
    for i in range(2, 98 + 1):
        # The larger multiplicand must have at least 3 digits (We could never reach a large enough result)
        for j in range(123, 9876 + 1):
            if _is_pandigital_product(i, j):
                results.add(i * j)

    return sum(results)


if __name__ == '__main__':
    print(problem_0032())
    # Expected: 45228

# IDEA Can I generate the ranges that already have unique numbers efficiently?
# There was the idea to check all permutations of 1-9, but that was a lot slower

# Maybe this can be made faster with tighter ranges on the positions as well?
# def problem_0032() -> int:
#     total = 0
#     results = set()
#     for l in permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9']):
#         for mul_pos in range(1, 8):
#             for equal_pos in range(mul_pos + 1, 9):
#                 multiplicand = int(''.join(l[0:mul_pos]))
#                 multiplier = int(''.join(l[mul_pos:equal_pos]))
#                 product = int(''.join(l[equal_pos:]))
#
#                 total += 1
#                 if multiplicand * multiplier == product:
#                     print(multiplicand, multiplier, product)
#                     results.add(product)
#
#     print(f'{total} options checked')
#     return sum(results)
