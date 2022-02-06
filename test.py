N, M = map(int, input().split())

result_list = []
used_node = [False] * N

def DFS(N, M, depth):
    if depth >= M:
        # print(*result_list)
        return
    for n in range(N):
        if used_node[n] == False:
            used_node[n] = True
            result_list.append(n+1)
            print(*result_list)
            DFS(N, M, depth+1)
            used_node[n] = False
            result_list.pop()
                
DFS(N, M, 0)