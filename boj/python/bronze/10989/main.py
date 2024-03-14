import sys

N = int(input())

count = [0] * 10001
for i in range(N):
    input_num = int(sys.stdin.readline())
    count[input_num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)