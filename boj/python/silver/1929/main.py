import sys
from math import sqrt

start, end = map(int, sys.stdin.readline().split())

prime_numbers = [True] * (end + 1)
prime_numbers[1] = False
divide = int(sqrt(end))

for i in range(2, divide + 1):
    if prime_numbers[i]:
        for j in range(i * 2, end + 1, i):
            prime_numbers[j] = False

for i in range(start, end + 1):
    if prime_numbers[i]:
        print(i)
