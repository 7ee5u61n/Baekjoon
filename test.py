n = int(input())

result = []
for i in range(1, n+1):
    arr = [n, i]
    j = 1
    while True:
        value = arr[j-1]-arr[j]
        if value < 0:
            break
        arr.append(value)
        j += 1
    
    if len(result) < len(arr):
        result = []
        result += arr

print(len(result))
print(*result)