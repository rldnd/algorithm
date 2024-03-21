import sys
readline = sys.stdin.readline

numbers = [int(readline()) for _ in range(9)]
line_dict = dict()

for index, number in enumerate(numbers):
    line = index + 1
    line_dict[number] = line

max_value = sorted(numbers)[-1]
print(max_value)
print(line_dict[max_value])