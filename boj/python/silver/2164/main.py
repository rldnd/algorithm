from collections import deque

N = int(input())
_deque = deque([i for i in range(1, N+1)])

while(len(_deque) > 1):
    _deque.popleft()
    _deque.append(_deque.popleft())
    
print(_deque[0])