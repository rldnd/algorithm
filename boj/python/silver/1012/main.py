import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check_closed_cabbage(arr: list, i: int, j: int, max_col: int, max_row: int):
    if arr[i][j] == 1:
        arr[i][j] = 0
        top, right, bottom, left = [i, j-1], [i+1, j], [i,j+1], [i-1, j]
        if not top[1] == -1:
            check_closed_cabbage(arr, top[0], top[1], max_col, max_row)
        if not right[0] > max_col:
            check_closed_cabbage(arr, right[0], right[1], max_col, max_row)
        if not bottom[1] > max_row:
            check_closed_cabbage(arr, bottom[0], bottom[1], max_col, max_row)
        if not left[0] == -1:
            check_closed_cabbage(arr, left[0], left[1], max_col, max_row)

test_cases = int(readline())
for _ in range(test_cases):
    width, height, cabbages = map(int, readline().split())
    cabbage_array = [[0 for _ in range(height)] for _ in range(width)]
    for _ in range(cabbages):
        col, row = map(int,readline().split())
        cabbage_array[col][row] = 1
        
    count = 0
    for i in range(width):
        for j in range(height):
            if cabbage_array[i][j] == 1:
                count += 1
                check_closed_cabbage(cabbage_array, i, j, width - 1, height - 1)
    
    print(count)