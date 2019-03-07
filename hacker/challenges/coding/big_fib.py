number = 1500000
digits = 20000

fib = [1, 1]

current_number = 2

for current_number in range(2, number):
    fib[current_number % 2] = sum(fib)

big_fib = fib[current_number % 2]

result = str(big_fib)
for i in range(0, len(result), digits):
    print(result[i], end='')
print()
