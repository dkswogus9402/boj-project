x, y, w, h = map(int, input().split())

A = w - x
B = h - y

print(min(A, B, x, y))
