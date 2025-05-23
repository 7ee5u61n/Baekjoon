n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
result = -1
for i in range(1, n):
    loc = i-1
    newItem = a[i]

    while loc >= 0 and newItem < a[loc]:
        count += 1
        a[loc+1] = a[loc]
        loc -= 1

        if count == k:
            result = a[loc+1]
            break

    if (loc+1 != i):
        count += 1
        a[loc+1] = newItem
            
        if count == k:
            result = a[loc+1]
            break

print(result)