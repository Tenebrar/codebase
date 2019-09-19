from functools import lru_cache

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


@lru_cache(maxsize=None)
def _ways_to_split(amount: int, prev_coin: int=COINS[-1]) -> int:
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # Only allow using coins in descending order to avoid permutations being counted multiple times
    return sum(_ways_to_split(amount - coin, coin) for coin in COINS if coin <= prev_coin)


def problem_0031(desired_value: int) -> int:
    # Warm the cache (I know each value will be needed, because 1 is in the coin options)
    for amount in range(1, desired_value + 1):
        _ways_to_split(amount)

    return _ways_to_split(desired_value)


if __name__ == '__main__':
    DESIRED_VALUE = 200

    print(problem_0031(DESIRED_VALUE))
    # Expected: 73682
