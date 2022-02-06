N, M = map(int, input().split())
result_list = [0] * M
cnt = 0

def DFS(N, M, depth):
    if depth >= M:
        print(*result_list)
        return

    for n in range(N):
            result_list[depth] = n + 1
            DFS(N, M, depth+1)

DFS(N, M, 0)