# N, M = map(int,input().split())
# result_list = [0] * M

# def DFS(N, M, depth):
#     if depth >= M:
#         for i in range(1, M):
#             if result_list[i-1] > result_list[i]:
#                 break
#         else:
#             print( *result_list )
#         return
#     for n in range(N):
#         result_list[depth] = n + 1
#         DFS(N, M, depth +1)

# DFS(N, M, 0)

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(*s) 
        return
    
    for i in range(start-1,n+1):
        s.append(i)
        dfs(i+1)
        s.pop()
dfs(2)