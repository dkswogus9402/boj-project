
cnt = 0
N = int(input())
A = [list(map(int, input())) for _ in range(N)]

def dfs(y, x):
    global cnt
    if 0 <= y < N and 0 <= x < N and A[y][x] == 1:
        cnt += 1
        A[y][x] = 0
        for dy, dx in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            dfs(y+dy, x+dx)

result = []
for i in range(N):
    for j in range(N):
        dfs(i,j)
        if cnt >= 1 :
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)
