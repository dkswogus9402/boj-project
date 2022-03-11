from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if A[i][j] == 1:
            queue.append([i,j])

pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while queue:
    i, j = queue.popleft()
    for dy, dx in pos:
        ny = dy + i
        nx = dx + j
        if 0 <= ny < N and 0 <= nx < M and A[ny][nx] == 0:
            queue.append([ny, nx])
            A[ny][nx] = A[i][j] + 1


flag = 0
max_value = -1
for i in range(N):
    for j in range(M):
        if max_value < A[i][j]:
            max_value = A[i][j]

        if A[i][j] == 0:
            flag = 1
            break


if flag == 1:
    print(-1)
else:
    print(max_value-1)