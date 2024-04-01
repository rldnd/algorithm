import sys
readline = sys.stdin.readline

def get_cases(number: int):
    if number == 1:
        return 1
    if number == 2:
        return 2
    if number == 3:
        return 4
    return get_cases(number - 1) + get_cases(number - 2) + get_cases(number - 3)

case_length = int(readline())
cases = [int(readline()) for _ in range(case_length)]

for number in cases:
    print(get_cases(number))