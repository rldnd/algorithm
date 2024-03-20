import sys
readline = sys.stdin.readline

while True:
    lines = list(map(int, readline().split()))
    if not lines[0] and not lines[1] and not lines[2]:
        break
    max_value = max(lines)
    lines.remove(max_value)
    print("right") if ((pow(lines[0], 2) + pow(lines[1], 2)) == pow(max_value, 2)) else print("wrong")