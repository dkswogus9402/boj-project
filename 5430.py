from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, 1+T):
    stack = deque(list(input().rstrip()))
    N = int(input())

    if N == 0:
        input_nums = input()
        queue = []
    else:
        input_nums = input()
        input_nums = input_nums[1:-2].split(',')
        queue = deque(input_nums)
    cnt = 0
    flag = 0
    while stack:
        command = stack.popleft()
        if command == 'R':
            cnt += 1
        elif command == 'D':
            if queue:
                if cnt % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                flag = 1
                break
    if flag == 1:
        print('error')
    else:
        if cnt % 2 == 0:
            print('['+ ','.join(queue) + ']' )
        else:
            queue.reverse()
            print('[' + ','.join(queue) + ']')