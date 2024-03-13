N = int(input())
base_list = set(map(int, input().split()))
M = int(input())
finding_list = list(map(int, input().split()))

for num in finding_list:
    print(1) if num in base_list else print(0)