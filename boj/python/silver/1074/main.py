import sys

N, target_row, target_col = map(int, sys.stdin.readline().split())
size = 2 ** N
row, col = 0, 0
result = 0

while not row == target_row or not col == target_col:
    section_size = ((size ** 2) // 4)
    current_divide_size = size // 2
    y, x = row + current_divide_size, col + current_divide_size
    if target_row < y and target_col >= x:
        col += current_divide_size
        result += section_size
    elif target_row >= y and target_col < x:
        row += current_divide_size
        result += section_size * 2
    elif target_row >= y and target_col >= x:
        row += current_divide_size
        col += current_divide_size
        result += section_size * 3
    
    N -= 1
    size = 2 ** N
    
print(result)