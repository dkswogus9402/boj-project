input_num = int(input())

num = 1
count = 0
while True:
    
    num += 1
    temp = str(num)
    if '666' in temp:
        count += 1

    if input_num == count:
        print(num)
        break