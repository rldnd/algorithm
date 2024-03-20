N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort()

for number in numbers:
    print(number)