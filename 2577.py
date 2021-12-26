A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_list = list(map(int,str(result))) # 문자열 -> 숫자로 바꾸면서 나눠짐

count_list = [0] * 10 # 파이썬 zeros

for num in result_list:
    count_list[num] += 1

for i in count_list:
    print(i)