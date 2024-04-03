# TODO: WIP
import sys

from itertools import combinations

readline = sys.stdin.readline

def get_combination_multiple(arr, length):
    count = 0
    combs = list(map(list, combinations(arr, length)))
    for lst in combs:
        mul = 1
        for item in lst:
            mul *= item
        count += mul
    return count
    
def get_count(clothes_count):
    types_clothes = {}
    clothes_count_with_types = []
    count = 0
    for _ in range(clothes_count):
        [_, types] = readline().rstrip().split()
        types_clothes[types] = types_clothes.get(types, 0) + 1
    for i in types_clothes.values():
        clothes_count_with_types.append(i)

    if len(clothes_count_with_types) == 1:
        return clothes_count_with_types[0]
    
    for i in range(1, len(clothes_count_with_types) + 1):
        count += get_combination_multiple(clothes_count_with_types, i)

    return count

test_cases = int(readline())
for _ in range(test_cases):
    clothes_count = int(readline())
    print(get_count(clothes_count))