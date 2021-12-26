A = []

for i in range(9):
    num = int(input())
    A.append(num)
max = A[0]
for i, num_ in enumerate(A):
    if num_ >= max:
        max = num_
        max_index = i+1

print(max)
print(max_index)