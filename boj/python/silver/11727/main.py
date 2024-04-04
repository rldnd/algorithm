import sys
n = int(sys.stdin.readline())
values = [0 for _ in range(1001)]
values[1] = 1
values[2] = 3
for i in range(3, 1001):
    values[i] =  values[i - 1] + 2 * values[i - 2]

print(values[n] % 10007)