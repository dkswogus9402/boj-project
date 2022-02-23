
'''
A  B  C  D  E  F
2  3  1  6  5  4 
3  1  2  4  6  5
5  6  4  1  3  2
1  3  6  2  4  5
4  1  6  5  2  3

-> 각 마주 보는 쌍을 기준으로 생각해야한다.

(A, F) (B, D) (C, E)  -> 처음 쌓는 것은 기준 X
 2  4   3  6   1  5

(A, F) (B, D) (C, E) -> C, E는 안됨
 3  5   1  4   2  6

(A, F) (B, D) (C, E) ->  B, D는 안됨
 5  2   6  1   4  3

(A, F) (B, D) (C, E) -> C, E는 안됨
 1  5   3  2   6  4

(A, F) (B, D) (C, E) -> C, E는 안됨
 4  3   1  5   6  2

'''
def face_to_face(i):
    if i == 0:
        return 5
    elif i == 1:
        return 3
    elif i == 2:
        return 4
    elif i == 3:
        return 1 
    elif i == 4:
        return 2
    elif i == 5:
        return 0


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

final = []
for i in range(6): # [2, 3, 1, 6, 5, 4]
    results = []
    result = []
    j = face_to_face(i)
    for jj in range(6):
        if jj == i or jj == j:
            continue
        result.append(A[0][jj])
    max_value = max(result)
    results.append(max_value)
    cnt = 1

    while cnt < N:
        for k in range(6):
            if A[cnt][k] == A[cnt-1][j]:
                break
        j = face_to_face(k)
        result = []
        for jj in range(6):
            if jj == k or jj == j:
                continue
            result.append(A[cnt][jj])
        cnt += 1
        max_value = max(result)

        results.append(max_value)
    final.append(sum(results))
print(max(final))

