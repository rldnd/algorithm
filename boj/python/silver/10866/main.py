import sys
from collections import deque
readline = sys.stdin.readline

lines = int(readline())
_deque = deque()

for _ in range(lines):
    line = readline().rstrip()
    if line.startswith('push_front'):
        _deque.appendleft(int(line.split()[1]))
    if line.startswith('push_back'):
        _deque.append(int(line.split()[1]))
    if line == 'pop_front':
        if not len(_deque): print(-1)
        else: print(_deque.popleft())
    if line == 'pop_back':
        if not len(_deque): print(-1)
        else: print(_deque.pop())
    if line == 'size':
        print(len(_deque))
    if line == 'empty':
        if not len(_deque): print(1)
        else: print(0)
    if line == 'front':
        if not len(_deque): print(-1)
        else: print(_deque[0])
    if line == 'back':
        if not len(_deque): print(-1)
        else: print(_deque[-1])
