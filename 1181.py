import sys

num = int(sys.stdin.readline().strip())
input_strs = []
for _ in range(num):
    input_str = sys.stdin.readline().strip()
    input_strs.append(input_str)
input_strs = set(input_strs)
input_strs = list(input_strs)
input_strs.sort()
input_strs.sort(key = len)

for value in input_strs:
    print(value)
