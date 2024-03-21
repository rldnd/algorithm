import sys
from math import factorial
[total, grab] = list(map(int, sys.stdin.readline().split()))

print(factorial(total) // (factorial(total - grab) * factorial(grab)))