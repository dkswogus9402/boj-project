#소수 덩어리#
prime_nums = []
for value in range(2, 10001):
    flag = 0
    for i in range(2, int(value**0.5) +1 ):
        if value % i == 0:
            flag = -1
            break
    if flag == 0:
        prime_nums.append(value)

input_num = int(input())

for o in range(input_num):
    # N은 2 보다 큰 짝수  
    N = int(input())

    num = N//2

    for k, value in enumerate(prime_nums):
        if value >= num:
            start = k
            break
    
    flag = -1

    while flag != 1:
        for j in range(start, -1, -1):
            if prime_nums[start] + prime_nums[j] < N:
                break
            elif prime_nums[start] + prime_nums[j] == N:
                flag = 1
                print(prime_nums[j], prime_nums[start])
        start += 1

