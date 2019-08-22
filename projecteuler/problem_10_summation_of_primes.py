MAXIMUM = 2000000

# Sieve of Eratosthenes is much faster if you need all primes to a given number
candidates = [i for i in range(MAXIMUM + 1)]
candidates[1] = 0

for candidate in candidates:
    if candidate > 1:
        for i in range(2, MAXIMUM // candidate + 1):
            candidates[i * candidate] = 0

print(sum(candidates))
# Expected: 142913828922
