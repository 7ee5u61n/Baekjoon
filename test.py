n = int(input())

arr = [0]*(n+1)
value = {0}

for i in range(1, n+1):
    if arr[i-1] - i < 0 or (arr[i-1] - i) in value:
        arr[i] = arr[i-1] + i
        value.add(arr[i])
    else:
        arr[i] = arr[i-1] - i
        value.add(arr[i])
    
print(arr[n])