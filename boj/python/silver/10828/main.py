import sys
readline = sys.stdin.readline

class Stack():
    def __init__(self):
        self._stack = []
        
    def size(self) -> int:
        return len(self._stack)

    def empty(self) -> int:
        if not self.size():
            return 1
        return 0
        
    def push(self, value: int) -> None:
        self._stack.append(value)
        
    def pop(self) -> int:
        if not self.empty():
            return self._stack.pop()
        return -1

    def top(self) -> int:
        if not self.empty():
           return self._stack[-1] 
        return -1

lines = int(readline())
stack = Stack()

for _ in range(lines):
    command = readline().rstrip()
    if command.startswith("push"):
        value = int(command.split()[1])
        stack.push(value)
    if command == 'pop':
        print(stack.pop())
    if command == 'size':
        print(stack.size())
    if command == 'empty':
        print(stack.empty())
    if command == 'top':
        print(stack.top())
    