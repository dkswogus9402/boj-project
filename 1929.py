A, B = map(int, input().split())
if A == 1:
    A = 2

for value in range(A,B+1):
    flag = 0
    for i in range(2, int(value ** 0.5) +1):
        if value % i == 0:
            flag = -1
            break
    if flag == 0:
        print(value)