N = int(input())
base_list = set(map(int, input().split()))
M = int(input())
finding_list = list(map(int, input().split()))

for num in finding_list:
    if num in base_list:
        print(1)
    else:
        print(0)