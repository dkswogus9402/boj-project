# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
from collections import deque
N = int(input())
queue = deque([N])
root = [0] * 1000001

while queue:
    num = queue.popleft()
    root_num = root[num]
    if num == 1:
        print(root_num)
        break

    if num % 3 == 0:
        new_num = num // 3
        if root[new_num] == 0:
            queue.append(new_num)
            root[new_num] = root_num + 1

    if num % 2 == 0:
        new_num = num // 2
        if root[new_num] == 0:
            queue.append(new_num)
            root[new_num] = root_num + 1

    new_num = num - 1
    if root[new_num] == 0:
        queue.append(new_num)
        root[new_num] = root_num + 1

