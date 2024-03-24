import sys
from collections import deque

readline = sys.stdin.readline

dfs_stack = []
dfs_visited = []

def DFS(graph, start):
    for next_point in graph[start]:
        if not next_point in dfs_visited:
            dfs_visited.append(next_point)
            dfs_stack.append(next_point)
            DFS(graph, next_point)

def BFS(graph, start):
    visited = []
    queue = deque()
    
    visited.append(start)
    queue.append(start)
    
    while queue:
        number = queue.popleft()
        for next_point in graph[number]:
            if not next_point in visited:
                visited.append(next_point)
                queue.append(next_point)
                   
    for number in visited:
        print(number,end=' ')
    print('')

points, lines, start_point = map(int, readline().split())
graph = [[] * (points * 1) for _ in range(points + 1)]

for _ in range(lines):
    i, j = map(int, readline().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
    graph[j].sort()

dfs_stack.append(start_point)
dfs_visited.append(start_point)
DFS(graph, start_point)
for number in dfs_visited:
    print(number, end=' ')
print()
BFS(graph, start_point)