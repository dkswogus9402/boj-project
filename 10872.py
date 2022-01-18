num = int(input())

def mul_num(num):
    if num == 0:
        return 1
    return num * mul_num(num -1)

result = mul_num(num)
print(result)
