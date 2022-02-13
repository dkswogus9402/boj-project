
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0

A.sort()
B.sort(reverse=True)
for i in range(N):
    total += A[i] * B[i]

print(total)
