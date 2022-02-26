N = int(input())
A = list(map(int, input().split()))

cnt_1 = cnt_2 = 1
max_value = 0
for i in range(N-1):

    if A[i] < A[i+1]:
        if max_value < cnt_2:
            max_value = cnt_2
        cnt_2 = 1
        cnt_1 += 1

    elif A[i] > A[i+1]:
        if max_value < cnt_1:
            max_value = cnt_1
        cnt_1 = 1
        cnt_2 += 1

    elif A[i] == A[i+1]:
        cnt_1 += 1
        cnt_2 += 1

if max_value < cnt_2:
    max_value = cnt_2
elif max_value < cnt_1:
    max_value = cnt_2

print(max_value)
