import sys
readline = sys.stdin.readline

item_count, problem_count = map(int, readline().split())
item_dict = dict()
reversed_item_dict = dict()

for i in range(item_count):
    index = i + 1
    name = readline().rstrip()
    item_dict[index] = name
    reversed_item_dict[name] = index

for _ in range(problem_count):
    line = readline().rstrip()
    try:
        number = int(line)
        print(item_dict[number])
    except:
        print(reversed_item_dict[line])