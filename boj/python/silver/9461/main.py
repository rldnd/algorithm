import sys
readline = sys.stdin.readline

line_length = [0 for _ in range(101)]
line_length[1] = 1
line_length[2] = 1
line_length[3] = 1

for i in range(4, 101):
    line_length[i] = line_length[i - 3] + line_length[i - 2]

test_cases = int(readline())
for _ in range(test_cases):
    print(line_length[int(readline())])