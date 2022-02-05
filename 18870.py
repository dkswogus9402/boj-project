import sys

num = int(sys.stdin.readline().rstrip())

input_list = list(map(int, sys.stdin.readline().rstrip().split()))

result_list = sorted(set(input_list))

result_dict = {}

for i, value in enumerate(result_list):
    result_dict[value] = i
    
for value in input_list:
    print(result_dict[value], end = ' ')