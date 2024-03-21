import sys
readline = sys.stdin.readline

lines = int(readline())
dots = [list(map(int, readline().split())) for _ in range(lines)]
dots.sort(key = lambda item: (item[0], item[1]))

for dot in dots:
    print(dot[0], dot[1])