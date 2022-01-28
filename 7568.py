# 사람 수
num = int(input())

mans = []
for i in range(num):
    weight, height = map(int, input().split())
    mans.append([weight, height])

cnt = []
for weight_a, height_b in mans:
    count = 1
    for weight_c, height_d in mans:
        if weight_a < weight_c and height_b < height_d:
            count += 1
    cnt.append(count)

print(*cnt)