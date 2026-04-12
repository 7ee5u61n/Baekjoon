k = int(input())
n = int(input())
boom = False
time = 0
for _ in range(n):
    t, z = map(str, input().split())
    if boom:
        continue
    time += int(t)
    if time >= 210:
        boom = True
        continue
    if z == 'T':
        k = (k+1) % 8

if k:
    print(k)
else:
    print(8)