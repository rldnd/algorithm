import sys
readline = sys.stdin.readline

def check_vps(line: str) -> bool :
    line_array = list(line)
    left, right = 0, 0
    for val in line_array:
        if val == "(":
            left += 1
        else:
            right += 1
        if right > left:
            print("NO")
            return
    print("NO") if not left == right else print("YES")
    
line_count = int(readline())
for _ in range(line_count):
    check_vps(readline().rstrip())