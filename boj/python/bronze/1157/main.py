import sys

# https://www.acmicpc.net/problem/1157

word = sys.stdin.readline().rstrip().lower()
obj = {}
for index in range(len(word)):
  value = obj.get(word[index], 0)
  obj[word[index]] = value + 1
  
max_value = max(obj.values())
max_keys = []
for key, value in obj.items():
  if value == max_value:
    max_keys.append(key)

if len(max_keys) > 1:
  print("?")
else:
  print(max_keys[0].upper())
