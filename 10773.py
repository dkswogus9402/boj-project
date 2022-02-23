
N = int(input())
nums = []

for i in range(N):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))