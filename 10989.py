import sys
input = sys.stdin.readline

num = int(input())
input_list = []
counting = {}

for _ in range(num):
    input_num = int(input())
    input_list.append(input_num)
    counting[input_num] = counting[input_num] + 1

result = [0] * num

total = 0
total_counting = {}
for key, value in counting.items(): # 누적 합
    total += value
    total_counting[key] = total

for number in input_list[::-1]: # 카운팅 합
    value = total_counting.get(number)
    result[value - 1] = number
    total_counting[number] -= 1

for value in result:
    print(value)
