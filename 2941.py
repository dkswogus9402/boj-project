import string

input_str = input()
table_two = ["dz=","c=", "c-", "d-", "lj", "nj", "s=", "z="]

# 문자열을 변경하는 함수 replace()

for str_ in table_two:
    input_str = input_str.replace(str_, "O")

print(len(input_str))
