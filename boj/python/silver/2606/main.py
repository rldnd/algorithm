import sys
from collections import deque
readline = sys.stdin.readline
    
total_computer_count = int(readline())
lines = int(readline())
connection_list = [[] for _ in range(total_computer_count + 1)]

for _ in range(lines):
    from_computer, to_computer = map(int, readline().split())
    connection_list[from_computer].append(to_computer)
    connection_list[to_computer].append(from_computer)

visited = [1]
_deque = deque()
_deque.append(1)

while _deque:
    item = _deque.popleft()
    for connected_computers in connection_list[item]:
        if not connected_computers in visited:
            visited.append(connected_computers)
            _deque.append(connected_computers)
    
visited.remove(1)
print(len(visited))