def w(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return w(num-3) + w(num - 2) + w(num - 1)


T = int(input())
for tc in range(1, 1+T):
    num = int(input())
    print(w(num))