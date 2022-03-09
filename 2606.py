N = int(input()) # 노드 개수
M = int(input()) # 간선
space = [ [] for _ in range(N+1)]
A = [list(map(int, input().split())) for _ in range(M)]
# 1차 정렬 양방향 연결이기 떄문에
for i in range(M):
    space[A[i][0]].append(A[i][1])
    space[A[i][1]].append(A[i][0])

computer_nums = [False] * (N+1)
computer_nums[1] = True
# 1번 컴퓨터가 바이러스에 걸림

def dfs(start):
    for i in space[start]:
        if computer_nums[i] == False:
            computer_nums[i] = True
            dfs(i)
dfs(1)
print(computer_nums.count(1)-1) # 1번을 제외한 수