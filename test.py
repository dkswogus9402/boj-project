def DFS(N, M, depth):
    global dfs_list
    global visited

    if depth >= M:
        print(*dfs_list)
        return

    else:
        for n in range(1, N+1):
            if visited[n-1] == False:
                visited[n - 1] = True
                dfs_list[depth] = n
                DFS(N, M, depth+1)
                visited[n - 1] = False

