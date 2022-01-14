num = input()
num = int(num)

input_strs = []

# input #
for i in range(num):
    input_str = input()
    input_strs.append(input_str)

# check word #
count = 0

for input_str in input_strs:
    list_strs = list(input_str)
    temp = []
    temp_str = 0
    flag = 0
    temp_len = len(list_strs)

    for i in range(temp_len):
        if temp_str == list_strs[0]:
            temp_str= list_strs.pop(0)
            continue
        for check in temp:
            if check in list_strs:
                flag = 1
                break
        if flag == 1:
            count += 1
            break

        temp.append(list_strs[0])
        temp_str= list_strs.pop(0)

result = num - count
print(result)

