A, B = map(int,input().split())
C, D = map(int,input().split())
E, F = map(int,input().split())

X = [A, C, E]
Y = [B, D, F]

for i in X:
    if X.count(i) == 1:
        x = i
        
for i in Y:
    if Y.count(i) == 1:
        y = i

print(x, y)