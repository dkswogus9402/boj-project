num = int(input())

for i in range(num):
    for k in range(num - i - 1):
        print(" ", end = "")
    for j in range(i+1):
        print("*", end = "")
    print()