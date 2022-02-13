T = int(input())

for tc in range(1,1+T):
    A, B = map(int,input().split())
    one = A ** 1 % 10
    two = A ** 2 % 10
    three = A ** 3 % 10
    four = A ** 4 % 10

    num = B % 4
    if one == 0:
        print(10)
    elif num == 1:
        print(one)
    elif num == 2:
        print(two)
    elif num == 3:
        print(three)
    else:
        print(four)
