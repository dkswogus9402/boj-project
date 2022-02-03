num = int(input())

list_x = []; list_y = []

for _ in range(num):
    x, y = map(int, input().split())
    list_x.append([x,y])
# 파이썬 다중 정렬을 사용할 수 있는가
list_x.sort(key = lambda x:(x[1],x[0])) 
for i in range(num):
    print(*list_x[i])