import sys
readline = sys.stdin.readline

number_count, line_count = map(int, readline().split())
numbers = list(map(int,readline().split()))
sum_numbers = [0 for _ in range(number_count + 1)]
sum_numbers[0] = numbers[0]
for index, number in enumerate(numbers):
    sum_numbers[index + 1] = sum_numbers[index] + numbers[index]

for _ in range(line_count):
    from_index, to_index = map(int, readline().split())
    print(sum_numbers[to_index] - sum_numbers[from_index - 1])