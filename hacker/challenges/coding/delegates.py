import math

value = 2118

sum_of_range = value * (value + 1) // 2
sum_of_squares = sum(x * x for x in range(int(math.sqrt(value)) + 1))

print(sum_of_range + sum_of_squares)
