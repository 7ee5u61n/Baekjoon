a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

dog = [0]*1000
for i in range(1000):
    if 0 < i % (a+b) <= a:
        dog[i] += 1
    if 0 < i % (c+d) <= c:
        dog[i] += 1

print(dog[p])
print(dog[m])
print(dog[n])