from collections import deque
import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(depth, cnt):
    global results
    if depth == 3:
        results.append(result[:])
        return
    for i in range(cnt, len(nums)):
        if visited[i] == False:
            visited[i] = True
            result[depth] = nums[i]
            dfs(depth+1, i)
            visited[i] = False

N, M = map(int, input().rstrip().split())
space = [ list(map(int, input().rstrip().split())) for _ in range(N)]

nums = []
wall_cnt = 0
# 후보가 될 수 있는 지점들
for i in range(N):
    for j in range(M):
        if space[i][j] == 0:
             nums.append([i, j])
        if space[i][j] == 1: # 벽인경우
            wall_cnt += 1
# 벽이 3개만 가능하다. -> 3개의 조합을 구해야함 중복 X
result = [0] * 3
visited = [False for _ in range(len(nums))]
results = []

dfs(0, 0)
# print(results)

# 바이러스가 퍼짐 -> BFS
virus = []
for i in range(N):
    for j in range(M):
        if space[i][j] == 2:
            virus.append([i, j])

pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# bfs에서 꺼낸 조합 하나씩 벽을 만들어줌

counts = []
for wall_1, wall_2, wall_3 in results:
    virus_num = len(virus) + wall_cnt + 3
    A = copy.deepcopy(space)
    y_1, x_1 = wall_1
    y_2, x_2 = wall_2
    y_3, x_3 = wall_3
    A[y_1][x_1] = A[y_2][x_2] = A[y_3][x_3] = 1

    queue = deque(virus)
    while queue:
        y, x = queue.popleft()
        for dy, dx in pos:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and A[ny][nx] == 0:
                A[ny][nx] = 2
                virus_num += 1
                queue.append([ny, nx])
    cnt = N*M - virus_num
    counts.append(cnt)

print(max(counts))