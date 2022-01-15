import math

num = int(input())

for i in range(num):
    x, y = map(int,input().split())
    length = y - x

    n = 0

    while True:
        if length <= n * (n+1):
            break
        n += 1

    if length > n ** 2:
        print(n * 2)
    else:
        print(n * 2 - 1)