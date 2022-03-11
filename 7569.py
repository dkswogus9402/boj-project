import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
A = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
pos = [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
queue = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if A[h][i][j] == 1: # 익은 토마토 지점을 찾았다면 넣는다.
                queue.append([h,i,j])

while queue:
    h, i, j = queue.popleft()
    for dz,dy,dx in pos:
        nz = h + dz
        ny = i + dy
        nx = j + dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and A[nz][ny][nx] == 0:
            queue.append([nz, ny, nx])
            A[nz][ny][nx] = A[h][i][j] + 1

max_value = A[0][0][0]
flag = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if A[h][i][j] == 0: # 익은 토마토 지점을 찾았다면 넣는다.
                flag = 1
                break

            if max_value < A[h][i][j]:
                max_value = A[h][i][j]

if flag == 1:
    print(-1)
else:
    print(max_value-1)