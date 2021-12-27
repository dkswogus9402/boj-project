input_nums = []
for i in range(10):
    temp = int(input())
    input_nums.append(temp)

count_nums = [0] * 42

for j in range(10):
    count = input_nums[j] % 42
    count_nums[count] = 1

result = sum(count_nums)

print(result)
