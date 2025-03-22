import sys
input = sys.stdin.readline

s = set()
m = int(input())

for i in range(1, m+1):
    oper = list(input().split())
    if oper[0] == 'add':
        s.add(oper[1])

    elif oper[0] == 'remove':
        if oper[1] in s:
            s.remove(oper[1])
    
    elif oper[0] == 'check':
        if oper[1] in s:
            print(1)
        else:
            print(0)
    
    elif oper[0] == 'toggle':
        if oper[1] in s:
            s.remove(oper[1])
        else:
            s.add(oper[1])
    
    elif oper[0] == 'all':
        s = set(str(i) for i in range(1, 21))
    
    elif oper[0] == 'empty':
        s = set()
