a = int(input())

for i in range(a):
    x, y = input().split()
    x = int(x)
    y = int(y)
    result = x + y
    print(f"Case #{i+1}:", result)