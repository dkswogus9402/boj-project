prime_nums = []

for value in range(2, 123457*2 +1):
    flag = 0
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            flag = -1
            break
    if flag == 0:
        prime_nums.append(value)

while True:
    num = int(input())
    if num == 0:
        break 
    count = 0
    for i, value in enumerate(prime_nums):
        if value > num:
            start = i
            break
        elif value == num:
            start = i + 1
            break

    for j, value in enumerate(prime_nums):
        if value >= 2 * num:
            end = j
            break

    result = end - start
    if num == 1:
        result = 1
    print(result)
