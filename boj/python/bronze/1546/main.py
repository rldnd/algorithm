import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

new_scores = list(map(lambda x: x / M * 100, scores))
average = sum(new_scores) / N
print(average)