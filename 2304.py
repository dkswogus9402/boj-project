N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

result = 0
max_value = A[0][1]
max_idx = A[0][0]
for idx, value in A:
    if max_value < value:
        max_value = value
        max_idx = idx

result += max_value
standard = max_idx
while True:
    candidates = []
    for idx, value in A:
        if idx < max_idx:
            candidates.append([idx, value])
    if candidates == []:
        break

    temp = max_idx
    max_value = 0
    for idx, value in candidates:
        if max_value < value:
            max_value = value
            max_idx = idx

    result += (max_value * abs(max_idx - temp))

max_idx = standard
while True:
    candidates = []
    for idx, value in A:
        if idx > max_idx:
            candidates.append([idx, value])
    if candidates == []:
        break
    temp = max_idx + 1
    max_value = 0
    for idx, value in candidates:
        if max_value < value:
            max_value = value
            max_idx = idx

    result += (max_value * abs(temp - (max_idx+1)))

print(result)



    




