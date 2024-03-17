import sys

def get_prime_numbers(max_value: int):
    prime_number = [True] * max_value
    maximum = int(max_value ** 0.5)
    for i in range(2, maximum + 1):
        if prime_number[i] == True:
            for j in range(2 * i, max_value, i):
                prime_number[j] = False
    return [i for i in range(2, max_value) if prime_number[i] == True]

readline = sys.stdin.readline
N = readline().rstrip()
numbers = list(map(int, readline().split()))
max_number = max(numbers)

prime_numbers = get_prime_numbers(max_number + 1)
count = 0
for number in numbers:
     if number in prime_numbers:
         count += 1
    
print(count)