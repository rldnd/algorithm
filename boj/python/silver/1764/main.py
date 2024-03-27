import sys
readline = sys.stdin.readline

not_seen_count, not_heard_count = map(int, readline().split())
person_dict = dict()
not_seen_heard_name_list = list()

for _ in range(not_seen_count):
    not_see_name = readline().rstrip()
    person_dict[not_see_name] = 1

for _ in range(not_heard_count):
    not_hear_name = readline().rstrip()
    person_dict[not_hear_name] = person_dict.get(not_hear_name, 0) + 1
    
for i in person_dict:
    if person_dict[i] == 2:
        not_seen_heard_name_list.append(i)
    
print(len(not_seen_heard_name_list))
not_seen_heard_name_list.sort()
for name in not_seen_heard_name_list:
    print(name)