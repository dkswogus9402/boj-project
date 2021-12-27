num = int(input())
for i in range(num):
    input_num = input() # 문자열 나누기 방법
    A = list(input_num)

    sum = 0
    count = 0

    for check in A:
        if check == "O":
            count += 1
            sum = sum + count
        else :
            count = 0

    print(sum)
