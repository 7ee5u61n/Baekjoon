from collections import deque

n = int(input())
a = []
b = []
c = []
waiting = deque()

for _ in range(n):
    s = list(map(int, input().split()))

    if s[0] == 1:
        waiting.append([s[1], s[2]])
    else:
        student, menu = waiting.popleft()
        
        if menu == s[1]:
            a.append(student)
        else:
            b.append(student)

for i in waiting:
    c.append(i[0])

if a:
    a.sort()
    print(*a)
else:
    print('None')
if b:
    b.sort()
    print(*b)
else:
    print('None')
if c:
    c.sort()
    print(*c)
else:
    print('None')