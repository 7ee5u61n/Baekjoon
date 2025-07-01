n, l = map(int, input().split())
street = [0] * (l+1)
for _ in range(n):
    d, r, g = map(int, input().split())
    street[d] = [r, g]
# print(street)
time = 0
distance = 0
while distance < l:
    if street[distance]:
        r, g = street[distance]
        if time % (r+g) >= r:
            distance += 1
    else:
        distance += 1

    time += 1

print(time)