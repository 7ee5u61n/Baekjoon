import sys
input = sys.stdin.readline

n = int(input())

calc = ''
for i in range(2*n-1):
    value = str(input().strip())
    if value == '/':
        value = '//'
    calc += value

print(eval(calc))