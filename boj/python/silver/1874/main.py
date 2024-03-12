N = int(input())
input_stack = list(range(1, N + 1))
current_stack = []
stack = []

print_stack = []

for _ in range(N):
    stack.append(int(input()))
    
while len(stack) != 0:
    output = stack[0]
    if len(current_stack) > 0 and current_stack[-1] == output:
        current_stack.pop()
        stack.remove(output)
        print_stack.append('-')
        continue
    
    if len(input_stack) == 0:
        print_stack.append('NO')
        break
    
    input = input_stack[0]
    input_stack.remove(input)
    
    if input <= output:
        current_stack.append(input)
        print_stack.append('+')
        continue
    else:
        print_stack.append('NO')
        break
    
if 'NO' in print_stack:
    print('NO')
else:
    for text in print_stack:
        print(text)