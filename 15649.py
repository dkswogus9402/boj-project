N, M = map(int, input().split())
dfs_list = [0] * M
visited = [False] * N # 방문했던 곳


def DFS(N, M, depth):
    global dfs_list

    if depth >= M:
        print(*dfs_list)
        return
    else:
        for n in range(1, N + 1):
            if visited[n - 1] == False: # 방문했던 곳
                visited[n - 1] = True
                dfs_list[depth] = n
                DFS(N, M, depth+1)
                visited[n - 1] = False # 다시 돌아가서 방문했던 곳 취소
DFS(N, M, 0)
