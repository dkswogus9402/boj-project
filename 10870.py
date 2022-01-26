num = int(input())

def Fibona(num):
    if num <= 1:
        return num
    return Fibona(num -1) + Fibona(num -2)

print(Fibona(num))
