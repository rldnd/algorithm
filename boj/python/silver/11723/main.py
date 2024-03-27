import sys
readline = sys.stdin.readline

lines = int(readline())
data = set()
full_data = set(map(str, range(1, 21)))

def handlecommand(command: str):
    if command.startswith("add"):
        data.add(command.split()[1])
    if command.startswith("remove"):
        number = command.split()[1]
        if number in data:
            data.remove(number)
    if command.startswith("check"):
        print(1 if (command.split()[1] in data) else 0)
    if command.startswith("toggle"):
        number = command.split()[1]
        handlecommand(f"add {number}") if (not number in data) else handlecommand(f"remove {number}")
    if command.startswith("all"):
        data.update(full_data)
    if command.startswith("empty"):
        _data = set(data)
        for key in _data:
            data.remove(key)

for _ in range(lines):
    command = readline().rstrip()
    handlecommand(command)
    
    