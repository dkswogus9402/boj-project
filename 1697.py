import sys
from collections import deque

queue = deque()
start, goal = map(int, input().split())
N = [0] * 100001
queue.append(start)
flag = 0

if start == goal:
    queue = []
    print(0)

while queue:
    result = queue.popleft()
    for data in [result+1, result-1, result*2]:
        if  0 <= data <= 100000 and N[data] == 0:
            queue.append(data)
            N[data] = N[result] + 1

            if data == goal:
                print(N[data])
                flag = 1
                break
    if flag == 1:
        break

