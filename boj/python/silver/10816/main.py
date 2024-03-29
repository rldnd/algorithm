import sys
from bisect import bisect_left, bisect_right
readline = sys.stdin.readline

owned_card_count = int(readline())
owned_cards = list(map(int, readline().split()))
finding_card_count = int(readline())
finding_cards = list(map(int, readline().split()))
owned_cards.sort()

for finding_card in finding_cards:
    print(bisect_right(owned_cards, finding_card) - bisect_left(owned_cards, finding_card))

