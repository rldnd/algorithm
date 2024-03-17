# TODO

import sys
readline = sys.stdin.readline

def checker(arr: list, order: int, count = 0):
    _count = count
    _arr = arr
    _order = order
    max_number = max(arr)
    first_number = _arr[0]
    
    if arr[0] == max_number:
        _count += 1
        if order == 0:
            print(_count)
            return
        del _arr[0]
        _order = len(_arr) - 1
    else:
        _arr.insert(len(_arr), first_number)
        if order == 0:
            _order = len(_arr) - 1
        else:
            _order -= 1
    checker(_arr, _order, _count)

test_case_count = int(readline().rstrip())
for _ in range(test_case_count):
    _, order = map(int, readline().rstrip().split())
    number_list = list(map(int, readline().rstrip().split()))
    checker(number_list, order)