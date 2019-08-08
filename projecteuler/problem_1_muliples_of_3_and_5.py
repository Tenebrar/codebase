MAXIMUM = 1000


def sum_multiples_of(value: int) -> int:
    """ Returns the sum of all multiples of a given number under MAXIMUM """
    amount = (MAXIMUM - 1) // value
    return amount * (amount + 1) // 2 * value


print(sum_multiples_of(3) + sum_multiples_of(5) - sum_multiples_of(15))
# Expected: 233168
