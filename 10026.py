# 적록색약은 빨간색과 초록색을 구분못함

# 크기가 N N인 그리드칸에 RGB 중 하나를 색칠한 그림이 있다.
# 그림은 몇 개의 구역으로 나뉘어져 있는데....구역은 같은 색으로 이루어져 있다.
# 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
# 색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라고 한다.

# 시작점은 0,0으로 시작
import copy
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(i,j, color, C):
    for dy, dx in pos:
        ny = i + dy
        nx = j + dx
        if 0 <= nx < N and 0 <= ny < N and C[ny][nx] == color :
            C[ny][nx] = 0
            dfs(ny, nx, color, C)


N = int(input())

A = [list(input().rstrip()) for _ in range(N)]
B = copy.deepcopy(A)


for i in range(N):
    for j in range(N):
        if B[i][j] == 'G':
            B[i][j] = 'R'

# 상하좌우로 이동
pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# 시작점은 0,0으로 시작 -> N.N 까지 확인해야함

cnt_1 = 0
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if A[i][j] != 0:
            dfs(i, j, A[i][j], A)
            cnt_1 += 1

        if B[i][j] != 0:
            dfs(i, j, B[i][j], B)
            cnt_2 += 1

print(cnt_1, cnt_2)