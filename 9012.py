N = int(input())

for i in range(N):
    A = input()
    stack = []
    cnt = 0
    for a in A:
        if a == '(':
            stack.append(a)
            cnt += 1
        elif a == ')':
            cnt -= 1
            if cnt >= 0:
                stack.pop()

    if cnt == 0 and len(stack) == 0:
        print('YES')
    else:
        print('No')