import sys
from collections import deque

def dfs(n):
    visited[n] = True
    results.append(n)
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        results.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())
graph = [] + [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]



print(graph)
results = []
visited = [False] * (N + 1)
dfs(V)
print(*results)

visited = [False] * (N + 1)
bfs(V)
print(*results)

