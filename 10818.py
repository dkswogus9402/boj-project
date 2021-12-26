N = map(int,input())
A = list(map(int, input().split()))

min, max = A[0], A[0]

for num in A:
    if num < min:
        min = num 
    if num > max:
        max = num 

print(min, max)