n, m = map(int, input().split())
a = list(map(int, input().split()))

diet = 0
day = -1
for i in range(n-1, -1, -1):
    diet += a[i]
    if diet >= m:
        day = i+1
        break
        
print(day)