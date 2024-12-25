n, k = map(int, input().split())
a = list(map(int, input().split()))

outlet = 0
for i in range(k):
    if a[i] % 2 == 0:
        outlet += a[i]//2
    else:
        outlet += a[i]//2+1
        
if outlet >= n:
    print('YES')
else:
    print('NO')