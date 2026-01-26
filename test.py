import sys
input = sys.stdin.readline

n, m = map(int, input().split())
classmate = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    classmate[a] += 1
    classmate[b] += 1

for i in range(1, n + 1):
    print(classmate[i])