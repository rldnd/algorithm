import sys

readline = sys.stdin.readline

A, B, C = map(int, readline().split())

def get_mod(a, b, c):
    if b == 1:
        return a % c
    pow = (get_mod(a, b//2, c) ** 2) % c
    if b % 2:
        return (pow * a) % c
    return pow

print(get_mod(A, B, C))