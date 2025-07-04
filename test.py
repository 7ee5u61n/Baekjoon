from collections import deque

n = int(input())
a = deque(map(int, input().split()))

count = 1
while len(a) > 1:
    x = a.popleft()
    if len(a) > 0:
        if (x+a[0])%2:
            count += 1
        else:
            a.popleft()
            a.appendleft(x)

print(count)