import sys

K, N = map(int, input().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
max_value = result = sum(A[:N])

for i in range(K - N):
    result = result - A[i] + A[i+N]
    if max_value < result:
        max_value = result
print(max_value)