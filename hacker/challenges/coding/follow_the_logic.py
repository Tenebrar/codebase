# Converted from javascript found in the source of the page
x = 2
y = 5
z = 3
a = [6, 5, 4, 9, 3, 7]
v = y * a[y] + z * a[z] - y * x * z + a[y] * a[x] * a[3]
# a.reverse()  # The call in javascript would not do anything
v = v + a[z] + a[y] + 11 * a[1] + a[0] - 1

print(v)
