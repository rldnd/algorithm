# MEMO: dynamic programming ( 점화식을 만들자 )

zero_count = [0] * 41
one_count = [0] * 41

zero_count[0] = 1
one_count[1] = 1

def fibonacci(n):
    for i in range(2, n + 1):
        zero_count[i] = zero_count[i - 2] + zero_count[i - 1]
        one_count[i] = one_count[i - 2] + one_count[i - 1]


t = int(input())

for i in range(t):
    n = int(input())

    fibonacci(n)

    print(zero_count[n], one_count[n])