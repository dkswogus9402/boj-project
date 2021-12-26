num = int(input())

for i in range(num):
    x, y = input().split()
    x = int(x)
    y = int(y)
    result = x + y

    print(f"Case #{i+1}: {x} + {y} = {result}")