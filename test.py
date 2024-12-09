def block(h):
    count = 0
    for i in range(n):
        if i < h:
            if tower[i] != (tower[h]-(h-i)*k):
                count += 1
        elif i > h:
            if tower[i] != (tower[h]+(i-h)*k):
                count += 1
    return count
        

n, k = map(int, input().split())
tower = list(map(int, input().split()))

result = 1000
for i in range(n):
    if tower[i] > i*k:
        result = min(result, block(i))

print(result)