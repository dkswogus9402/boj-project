def draw_ster(n):
    # escape 문
    global result
    if n == 3:
        result[2][0:3] = result[0][0:3] = [1, 1, 1]
        result[1][0:3] = [1, 0, 1]
        return

    num = n//3
    draw_ster(num)
    for row in range(3):
        for column in range(3):
            if row == 1 and column == 1:
                continue
            for k in range(num):
                result[num * row + k][num * column : num * (column + 1)] = result[k][:num]

n = int(input())
result = [[0 for i in range(n)] for j in range(n)]
draw_ster(n)

for value in result:
    for i in value:
        if i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()