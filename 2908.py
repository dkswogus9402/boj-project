import string 
a, b = input().split()
a = list(a)
b = list(b)

a = a[::-1]
b = b[::-1]

for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])


new_a = a[0] * 100 + a[1] * 10 + a[2] * 1
new_b = b[0] * 100 + b[1] * 10 + b[2] * 1

if new_a > new_b:
    print(new_a)
else:
    print(new_b)