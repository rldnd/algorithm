from math import ceil

A, B, V = map(int, input().split())
try_count, current_height = 0, 0
once_height = A - B

print(ceil((V - A) / once_height) + 1)