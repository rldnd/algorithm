from sys import stdin

class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

head = ListNode('dummy', None, None)
curr = head

init = input()
for i in range(len(init)):
    new_node = ListNode(init[i], None, None)
    curr.next = new_node
    new_node.prev = curr
    curr = new_node

for _ in range(int(input())):
    command = stdin.readline().rstrip()
    if command == 'L':
        if curr.val != 'dummy':
            curr = curr.prev
    elif command == 'D':
        if curr.next:
            curr = curr.next
    elif command == 'B':
        if curr.val != 'dummy':
            curr = curr.prev
            if curr.next.next:
                curr.next = curr.next.next
                curr.next.prev = curr
            else:
                curr.next = None
    else:
        new_node = ListNode(command[-1], None, None)
        if curr.next:
            new_node.next = curr.next
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        curr = new_node

print_node = head.next
while print_node:
    print(print_node.val, end='')
    print_node = print_node.next