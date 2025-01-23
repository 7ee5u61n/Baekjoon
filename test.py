n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(n-1, 0, -1):
    max_index = i
    for j in range(i):
        if arr[max_index] < arr[j]:
            max_index = j

    if arr[i] != arr[max_index]:
        arr[i], arr[max_index]= arr[max_index], arr[i]
        count += 1
    
    if count == k:
        break

if count < k:
    print(-1)
else:
    print(*arr)