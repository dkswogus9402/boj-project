N = int(input())

result = 0
for i in range(N):
    total = 0
    list_N = list(str(i))
    int_N = int(i)

    for value in list_N:
        total += int(value)
    total += int_N

    if total == N:
        result = int_N
        break
print(result)