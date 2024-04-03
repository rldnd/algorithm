import math
number_array = [0 for _ in range(100001)]

def get_cd(value):
    divider = math.floor(value ** (1/2))
    for i in range(1, divider + 1):
        if i ** 2 == value:
            number_array[value] += 1
        elif value % i == 0:
            number_array[value] += 2

def solution(number, limit, power):
    total_power = 0
    
    for value in range(number + 1):
        get_cd(value)
        
    for num in number_array[1:number+1]:
        if num > limit:
            total_power += power
        else:
            total_power += num
    
    return total_power