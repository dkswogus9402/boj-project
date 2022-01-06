num = int(input())

A_1 = 1
n = 1
while True:
    result = A_1 + n/2 * (n-1) * 6
    if result >= num:
        break
    n += 1
print(n)