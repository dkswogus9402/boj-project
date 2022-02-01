import sys
input = sys.stdin.readline

def Divide(input_list):
    len_list = len(input_list)
    if len_list <= 1:
        return input_list

    new_length = len_list // 2
    
    left = Divide(input_list[:new_length])
    right = Divide(input_list[new_length:])

    i, j= 0,0
    result = []

    while i<len(left) and j <len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i != len(left):
        result += left[i:]
    elif j != len(right):
        result += right[j:]

    return result

num = int(input())

input_list = []

for i in range(num):
    input_num = int(input())
    input_list.append(input_num)
result = Divide(input_list)

for value in result:
    print(value)