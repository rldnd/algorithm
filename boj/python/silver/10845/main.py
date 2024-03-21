import sys
readline = sys.stdin.readline

class Queue():
    def __init__(self):
        self._queue = []
        
    def size(self):
        return len(self._queue)

    def empty(self):
        if not self.size():
            return 1
        return 0
        
    def push(self, value: int):
        self._queue.append(value)
    
    def pop(self):
        if self.empty():
            return -1
        pop_value = self._queue[0]
        del self._queue[0]
        return pop_value

    def front(self):
        if self.empty():
            return -1
        return self._queue[0]
        
    def back(self):
        if self.empty():
            return -1
        return self._queue[-1]
    
lines = int(readline())
queue = Queue()
for _ in range(lines):
    line = readline().rstrip()
    if line.startswith('push'):
        value = int(line.split()[1])
        queue.push(value)
    if line == 'pop':
        print(queue.pop())
    if line == 'size':
        print(queue.size())
    if line == 'empty':
        print(queue.empty())
    if line == 'front':
        print(queue.front())
    if line == 'back':
        print(queue.back())