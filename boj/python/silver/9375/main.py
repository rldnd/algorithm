import sys
readline = sys.stdin.readline

test_cases = int(readline())
for _ in range(test_cases):
    result = 1
    clothes_count = int(readline())
    types_count_map = {}
    for _ in range(clothes_count):
        types = readline().rstrip().split()[1]
        types_count_map[types] = types_count_map.get(types, 0) + 1
    for value in types_count_map.values():
        result *= (value + 1)
    print(result - 1)