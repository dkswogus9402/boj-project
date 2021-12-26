
x = int(input())
count = 0

temp = x
while(1):
    ten_num = temp // 10
    one_num = temp % 10
    new_num = ten_num + one_num
    new_num = new_num % 10
    new_num = one_num * 10 + new_num
    temp = new_num
    count += 1
    if temp == x:
        print(count)
        break