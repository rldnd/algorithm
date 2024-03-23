import sys
from collections import deque

readline = sys.stdin.readline
test_cases = int(readline())

x = [0, 1, 0 ,-1]
y = [1, 0, -1, 0]

def BFS(cabbage_array, i, j, visited, max_col, max_row):
    _deque = deque([(i, j)])
    visited[i][j] = 1
    while _deque:
        col, row = _deque.popleft()
        for i in range(4):
            ix = col + x[i]
            iy = row + y[i]
            if ix > max_col or iy > max_row or ix < 0 or iy < 0:
                continue
            if cabbage_array[ix][iy] and not visited[ix][iy]:
                visited[ix][iy] = 1
                _deque.append((ix, iy))

for _ in range(test_cases):
    width, height, cabbages = map(int, readline().split())
    cabbage_array = [[0] * height for _ in range(width)]
    visited = [[0] * height for _ in range(width)]
    
    for _ in range(cabbages):
        col, row = map(int, readline().split())
        cabbage_array[col][row] = 1
        
    result = 0
    for i in range(width):
        for j in range(height):
            if cabbage_array[i][j] and not visited[i][j]:
                result += 1
                BFS(cabbage_array, i, j, visited, width - 1, height - 1)
            
    print(result)
    