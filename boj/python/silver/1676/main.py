from math import factorial

N = int(input())
reversed_factorial = str(factorial(N))[::-1]

zero_count = 0
for char in reversed_factorial:
    if char != "0":
        break
    zero_count += 1
    
print(zero_count)