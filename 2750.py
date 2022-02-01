import time

num = int(input())

input_nums = []
for i in range(num):
    input_num = int(input())
    input_nums.append(input_num)
start = time.time()

def new_sort(input_nums):
        
    len_nums = len(input_nums)  

    for i in range(1, len_nums+1):
        for idx in range(len_nums - i):
            if input_nums[idx] > input_nums[idx+1]:
                input_nums[idx], input_nums[idx+1] = input_nums[idx+1], input_nums[idx]
    return input_nums

results = new_sort(input_nums)
end = time.time()

print(end-start)
for result in results:
    print(result)
