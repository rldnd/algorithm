N = int(input())

count = 0
number = 666
fixed_number = 666
while True:
    if str(fixed_number) in str(number):
        count += 1
    if count == N:
        print(number)
        break
    number += 1