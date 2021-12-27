num = int(input())
for i in range(num):
    a, b = input().split()
    a = int(a)
    b = list(b)

    for str_ in b:
        for i in range(a):
            print(str_, end="")
    print()