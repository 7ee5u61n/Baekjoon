from collections import deque
import queue

s = str(input())
n = int(input())

count = 0
for _ in range(n):
    ring = (str(input())*2)
    for i in range(len(ring)):
        if ring[i:i+len(s)] == s:
            count += 1
            break
        
print(count)