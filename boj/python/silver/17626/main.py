import sys
import math

value = int(sys.stdin.readline())

dp = [0,1]

for i in range(2, value + 1):
    sqrted_value = math.floor(i ** (1/2))
    min_value = 1e9
    for j in range(1, sqrted_value + 1):
        min_value = min(min_value, dp[i - (j ** 2)])
    dp.append(min_value + 1)

print(dp[value])

