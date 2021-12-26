import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    x, y = sys.stdin.readline().rstrip().split()
    x = int(x)
    y = int(y)
    print(x+y)
