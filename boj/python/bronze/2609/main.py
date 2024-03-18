N, M = map(int, list(input().split()))
[small, large] = sorted([N, M])

def gcd(m: int, n: int):
    if not m % n:
        return n
    return gcd(n, m % n)

print(gcd(large, small))
print((large * small) // gcd(large, small))