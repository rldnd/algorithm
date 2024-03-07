a = input()
while a != '0':
    if a == '0':
        break
    if a == a[::-1]:
        print('yes')
    else:
        print('no')
    a = input()