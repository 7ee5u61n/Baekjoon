T = int(input())

for _ in range(T):
    s = str(input())
    for i in range(len(s)):
        print(s[i], end='')
        if s[i:i+2] == 'PO':
            print('H', end='')
    print('')