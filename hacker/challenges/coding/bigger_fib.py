from numpy import log

number = 150000000

PHI = (1 + 5 ** 0.5) / 2

# Estimate the number using this rule using the golden ratio
# estimate = (PHI ** number) / (5 **0.5)
# print(estimate)
# print(log(estimate))

# Use logarithm rules to get the desired result
result = number * log(PHI) - 0.5 * log(5)

print(f'{result:.3f}')
