s = list(input())
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]

for i in s:
    print(i, end='')