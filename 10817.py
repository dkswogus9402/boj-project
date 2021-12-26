N, X = input().split()
N = int(N)
X = int(X)

A = list(map(int, input().split()))

for num in A:
    if X > num:
        print(num, end = " ")