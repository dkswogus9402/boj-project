num = int(input())

result = -1
bag_3kg = 0

while num >= 0:
    if num % 5 == 0:
        bag_5kg = num // 5
        result = bag_5kg + bag_3kg
        break
    num = num - 3 # 3의 가방이 한개씩 늘어남
    bag_3kg += 1

if result != -1:
    print(result)
else:
    print(-1)