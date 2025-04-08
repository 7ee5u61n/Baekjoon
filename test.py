from collections import deque

n = deque(input())
first = deque(n)

result = 0
while True:
    n.appendleft(n.pop())
    result += int(''.join(n))

    if n == first:
        break

print(result)