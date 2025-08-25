import sys
input = sys.stdin.readline

n = int(input())
s = str(input().rstrip())

a = 0
b = 0

for i in s:
    if i == '2':
        a += 1
    else:
        b += 1

if a > b:
    print('2')
elif a < b:
    print('e')
else:
    print('yee')