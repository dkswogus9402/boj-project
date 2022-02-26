# 일곱난쟁이 키 합 100임


A = [int(input()) for _ in range(9)]
visited = [False] * 9
flag = 0
result = [0] * 7
def dfs(depth, j):
    global flag
    if flag == 1:
        return

    if depth == 7:
        if sum(result) == 100:
            new_result = sorted(result)
            for k in new_result:
                print(k)
            flag = 1
        return

    for i in range(j, 9):
        if visited[i] == False:
            visited[i] = True
            result[depth] = A[i]
            dfs(depth + 1, i)
            visited[i] = False

dfs(0, 0)