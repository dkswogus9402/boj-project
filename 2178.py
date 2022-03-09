N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]

# 출발 점은 1,1 임
y, x = 0, 0
queue = [[y,x]]
pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
root = [[False for _ in range(M)] for _ in range(N)]
root[y][x] = 1

while queue:
    y, x = queue.pop(0)
    # print('방문순서 : ', y, x)
    # print('Q :', queue)
    # print('count : ', root[y][x])
    for dy, dx in pos:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < N and 0 <= nx < M and A[ny][nx] != 0 and root[ny][nx] == False:
            queue.append([ny,nx]) # 인접한 것들 담아줌
            root[ny][nx] = root[y][x] + 1 # 방문했던 곳은 제외해줌

print(root[N-1][M-1])

