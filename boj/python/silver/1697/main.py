import sys
from collections import deque
readline = sys.stdin.readline

N, K = map(int, readline().split())
queue = deque()
visited = [0 for _ in range(200001)]

queue.append(N)
visited[N] = 1
res = 0

def get_enable(position):
    return [position - 1, position + 1, position * 2]

while queue:
    position = queue.popleft()
    for i in get_enable(position):
        if i > 200000 or i < 0:
            continue
        if visited[i] == 0 or visited[i] > visited[position] + 1:
            queue.append(i)
            visited[i] = visited[position] + 1
        
print(visited[K] - 1)