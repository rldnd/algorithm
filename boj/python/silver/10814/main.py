import sys
readline = sys.stdin.readline

lines = int(readline())
people = [readline().split() for _ in range(lines)]
people.sort(key = lambda item: int(item[0]))

for person in people:
    print(person[0], person[1])