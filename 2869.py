A, B, C = map(int, input().split())

result = (C-B) // (A-B)

if (C-B) % (A-B) != 0:
    print(result+1)
else:
    print(result)