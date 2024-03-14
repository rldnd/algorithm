import sys

N = int(input())
numbers = list(map(int, sys.stdin.readlines()))
numbers.sort()
for number in numbers:
    print(number)
    