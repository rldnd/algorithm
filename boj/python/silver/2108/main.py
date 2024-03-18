import sys
readline = sys.stdin.readline

count = int(readline())
numbers = [int(readline()) for _ in range(count)]
numbers.sort()
number_sum = sum(numbers)
print(round(number_sum / count))
print(numbers[(count // 2)])

frequent = {}
for number in numbers:
    frequent[number] = frequent.get(number, 0) + 1
frequent_max_value = max(frequent.values())
frequent_max_keys = []
for number, frequency in frequent.items():
    if frequent_max_value == frequency:
        frequent_max_keys.append(number)

if (len(frequent_max_keys) > 1):
    frequent_max_keys.remove(min(frequent_max_keys))
    print(min(frequent_max_keys))
else:
    print(frequent_max_keys[0])
    

print(numbers[-1] - numbers[0])