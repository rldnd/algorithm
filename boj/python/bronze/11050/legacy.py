from itertools import combinations

lst = list(map(int, input().split()))
print(len(list(combinations(range(lst[0]), lst[1]))))