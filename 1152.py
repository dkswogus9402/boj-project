import string

input_str_ = input()
# 초기화 #
temp1 = 0
temp2 = 0

input_str = list(input_str_)

# 앞 쪽 빈칸 체크 #
for i, str_ in enumerate(input_str):
    if str_ != " ":
        temp1 = i
        break
input_reverse  = input_str[::-1]
# 뒤 쪽 빈칸 체크 #
for i, str_ in enumerate(input_reverse):
    if str_ != " ":
        temp2 = i
        break
count = 1
len_temp = len(input_str)-temp2

for j in range(temp1, len_temp):
    if input_str[j] == " ":
        count += 1
# 예외 처리 #
if input_str_ == " ":
    print(0)
else :
    print(count)