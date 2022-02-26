N = int(input())

A = [list(map(int, input().split())) for _ in range(6)]
# 두 개인 것을 찾기
result = []
flag = 0
while flag != 1:
    for i in range(len(A)-3):
        if A[i][0] == A[i+2][0] and A[i+1][0] == A[i+3][0]:
            result.append(A[i+1])
            result.append(A[i+2])
            flag = 1
            break
    A.append(A[0])
    A = A[1:]

test = {}
for pos, length in A:
    test[pos] = 0 if test.get(pos) else length

for key, value in test.items():
    if value != 0:
        result.append([key, value])

area = result[2][1] * result[3][1]
del_area = result[0][1] * result[1][1]
final = area - del_area
final = final * N
print(final)