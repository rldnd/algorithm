import math

def get_cd(value):
    cd_list = []
    divider = math.floor(value ** 1/2)
    for i in range(1, divider + 1):
        if value % i == 0:
            cd_list.append(i)
            
    return cd_list

def get_yellow_size_list(value):
    cd_list = get_cd(value)
    size_list = []
    for item in cd_list:
        size_list.append(item * (value // item))
        
    return size_list

def solution(brown, yellow):    
    sumation = brown + yellow
    cd_list = get_cd(sumation)
    yellow_size_list = get_yellow_size_list(yellow)
    
    if yellow == 1:
        return [sumation ** (1/2), sumation ** (1/2)]
    
    for cd in cd_list:
        base_width, base_height = cd, sumation // cd
        width, height = base_width - 2, base_height - 2
        size = width * height
        
        if size in yellow_size_list:
            return [max(base_width, base_height), min(base_width, base_height)]