num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    if H * W < N:
        print("방이 없습니다.")
        continue
    elif N % H != 0:
        Y = N % H
        X = N // H + 1

    else:
        Y = H
        X = N // H

    print(f"{Y}{X:02d}")
