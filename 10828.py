class stack:
    def __init__(self, size):
        self.memory = [0] * size
        self.top = -1
        self.size = size - 1 # 인덱스는 0부터 시작하므로

    def insert(self, value):
        if self.top < self.size:
            self.top += 1
            self.memory[self.top] = value
        else:
            print('꽉 차있습니다.')
        return

    def delete(self):
        if self.top > -1:
            temp = self.memory[self.top] # 선택과정
            self.memory[self.top] = 0 # 선택과정
            self.top -= 1
            return temp
        else:
            return -1

    def isEmpty(self):
        if self.top == -1:
            return 1
        else:
            return 0

    def peek(self):
        if self.top > -1:
            return self.memory[self.top]
        else:
            return -1

    def print_stack(self):
        if self.top == -1:
            print('비어있습니다.')
            return
        print(self.memory[:self.top+1])
        return

    def sizer(self):
        print(self.top + 1)
        return self.top
        
import sys
memory = stack(10000)

N = int(sys.stdin.readline())

for i in range(N):
    order = sys.stdin.readline().strip()
    
    if order[:4] == 'push':
        item = int(''.join(order[4:]))
        memory.insert(item)
    elif order == 'pop':
        print(memory.delete())
    elif order == 'size':
        memory.sizer()
    elif order == 'empty':
        print(memory.isEmpty())
    elif order == 'top':
        print(memory.peek())