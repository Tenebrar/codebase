# The golden ratio approximation could be used, but I felt these numbers were too small to warrant it

# The sequence has a repeating pattern of 'odd, odd, even', but there seems to be no real way of using that
# It could avoid the modulo check for evenness, but it's not like that is such a heavy operation anyway

MAXIMUM = 4000000

fib = [1, 2]  # Starting the sequence with these numbers is strange to me, but that is the assignment
index = 0
result = 2

while True:
    fib[index] = sum(fib)

    if fib[index] > MAXIMUM:
        break
    if fib[index] % 2 == 0:
        result += fib[index]

    index = 1 - index

print(result)
