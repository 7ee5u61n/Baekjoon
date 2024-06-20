import sys

T = int(input())

for _ in range(T):
    parenthesis = sys.stdin.readline().rstrip()
    
    while '()' in parenthesis:
        parenthesis = parenthesis.replace('()', '')
    
    if parenthesis:
        print('NO')
    else:
        print('YES')