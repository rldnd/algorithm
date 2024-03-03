import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())
  print(int(int(math.factorial(M)) / (int(math.factorial(N) * math.factorial(M-N)))))