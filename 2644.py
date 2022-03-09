N = int(input())
target = list(map(int, input().split()))
space = [[] for _ in range(N+1)]
root = [0] * (N+1)
queue = [target[0]]

T = int(input())
A = [ list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    space[A[i][0]].append(A[i][1])
    space[A[i][1]].append(A[i][0])

while queue:
    data = queue.pop(0)
    for i in space[data]:
        if root[i] == 0:
            root[i] = root[data] + 1
            queue.append(i)

if root[target[1]] != 0:
    print(root[target[1]])
else:
    print(-1)
