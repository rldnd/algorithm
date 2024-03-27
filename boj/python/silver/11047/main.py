import sys
readline = sys.stdin.readline

lines, goal_money = map(int, readline().split())
money_list = list()
count = 0
for _ in range(lines):
    money_list.append(int(readline()))

for money in money_list[::-1]:
    if goal_money == 0:
        break
    _count = goal_money // money
    goal_money -= (money * _count)
    count += _count

print(count)