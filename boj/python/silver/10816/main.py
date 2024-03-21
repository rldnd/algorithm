import sys
readline = sys.stdin.readline

owned_card_count = int(readline())
owned_cards = list(map(int, readline().split()))
finding_card_count = int(readline())
finding_cards = list(map(int, readline().split()))

owned_card_obj = {}
for owned_card in owned_cards:
    owned_card_obj[owned_card] = owned_card_obj.get(owned_card, 0) + 1

for finding_card in finding_cards:
    print(owned_card_obj.get(finding_card, 0))