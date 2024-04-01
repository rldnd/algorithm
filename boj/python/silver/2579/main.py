import sys
readline = sys.stdin.readline

stair_count = int(readline())
stairs = [0] * 301
for i in range(stair_count):
    stairs[i] = int(readline())
dp = [0] * 301

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0], stairs[1]) + stairs[2]

for i in range(3, stair_count):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
print(dp[stair_count - 1])