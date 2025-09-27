n = int(input())
plan = list(map(int, input().split()))

time = 0
for i in range(n):
    time += plan[i]
    if i < len(plan)-1:
        time += 8

d = time // 24
h = time % 24

print(d)
print(h)