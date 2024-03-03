# https://www.acmicpc.net/problem/1010
# Combination을 이용하여 풀이

import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())
  print(int(int(math.factorial(M)) / (int(math.factorial(N) * math.factorial(M-N)))))