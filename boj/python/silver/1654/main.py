# TODO binary search

import sys

num_exist_cable, num_require_cable = map(int, sys.stdin.readline().split())
exist_cables = []
for i in range(num_exist_cable):
    exist_cables.append(int(sys.stdin.readline()))

min_len, max_len = 1, max(exist_cables)
while min_len <= max_len:
    cut = (min_len+max_len) // 2
    num_cables = 0
    for cable in exist_cables:
        num_cables += cable // cut
    if num_cables >= num_require_cable:
        min_len = cut+1
    else:
        max_len = cut-1
        
print(max_len)