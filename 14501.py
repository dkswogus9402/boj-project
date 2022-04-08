N = int(input())
A = [[0, 0]]
for i in range(N):
    a = list(map(int, input().split()))
    if N+1 - a[0] >= i+1:
        A.append(a)
print(A)

def dfs(time, ssum):
    global max_value

    if time <= N+1:
        if max_value < ssum:
            max_value = ssum
    else:
        return

    for i in range(time, len(A)):
        if i+1 <= len(A)-1:
            print(i, ssum)
            print(i + A[i+1][0], ssum + A[i+1][1])
            print(A[i+1][0], A[i+1][1])
            dfs(i + A[i+1][0], ssum + A[i+1][1])

max_value = 0
for i in range(1, len(A)):
    print(i, A[i][0], A[i][1])
    dfs(A[i][0], A[i][1])
    print()

print(max_value)
