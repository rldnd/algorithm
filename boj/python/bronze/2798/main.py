import sys
from itertools import combinations
readline = sys.stdin.readline

card_count, max_value = map(int, readline().split())
cards = list(map(int, readline().split()))
temp_max_value = 0

for combination in combinations(cards, 3):
    if sum(combination) <= max_value:
        temp_max_value = max(temp_max_value, sum(combination))
        
print(temp_max_value)