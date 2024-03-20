import sys
readline = sys.stdin.readline

card_count, max_value = map(int, readline().split())
cards = list(map(int, readline().split()))
temp_max_value = 0

for i in range(card_count - 2):
    for j in range(i + 1, card_count - 1):
        for k in range(j + 1, card_count):
            sumations = cards[i] + cards[j] + cards[k]
            if sumations > temp_max_value and sumations <= max_value:
                temp_max_value = sumations

print(temp_max_value)