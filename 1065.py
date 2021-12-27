nums = int(input())

count = 0
for num in range(nums):
    if num+1 < 100:
        count += 1
        continue

    nums = list(map(int,str(num+1)))
    cha_1 = nums[0] - nums[1]
    cha_2 = nums[1] - nums[2]
    if cha_1 == cha_2:
        count += 1
print(count)


