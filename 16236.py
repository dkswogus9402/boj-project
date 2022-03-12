from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [ list(map(int, input().split())) for _ in range(N)]

root = [[0 for _ in range(N)] for _ in range(N)]

# 시작지점 찾기
queue = deque()
for i in range(N):
    for j in range(N):
        if A[i][j] == 9:
            A[i][j] = 0
            queue.append([i, j])
            break

# 함수를 만듬 좌표를 주면 주변에 관련해서 먼저 접근하는 녀석

def eat_fish(queue, size):
    pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    max_length = 100000
    candidate = []
    while queue:
        i, j = queue.popleft()
        if root[i][j] > max_length: # 만약에 지정해둔 것보다 큰 수가 나오면 종료
            break
        for dy, dx in pos:
            ny = dy + i
            nx = dx + j
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] <= size and root[ny][nx] == 0:
                if 0 < A[ny][nx] < size: # 꿀꺽
                    if root[i][j] < max_length:
                        candidate.append([ny,nx])
                        max_length = root[i][j] + 1
                queue.append([ny, nx])
                root[ny][nx] = root[i][j] + 1

    if candidate == []:
        return -1, -1, -1 # 후보가 더 이상 없음

    candidate.sort()
    i, j = candidate[0]
    return i, j, max_length

size = 2
cnt = 0
count = 0
while True:
    i, j, max_length = eat_fish(queue, size)

    if i == -1:
        break
    cnt += 1
    A[i][j] = 0 # 먹음

    root = [[0 for _ in range(N)] for _ in range(N)]
    count += max_length

    queue = deque([[i, j]])
    if cnt == size:
        size += 1
        cnt = 0

print(count)

