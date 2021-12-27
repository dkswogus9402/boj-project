import string

input_str = input()
input_str = input_str.upper()
input_str = list(input_str)
result = {}

# dict init #
for str_ in input_str:
    result[str_] = 0
# count add #
for str_ in input_str:
    result[str_] += 1

max = 0
max_index = 0
# search max #
for i in result:
    if max < result[i]:
        max = result[i]
        max_index = i

count = 0
# search max num #
for i in result:
    if max == result[i]:
        count += 1
# print #
if count > 1:
    print("?")
else:
    print(max_index)
    