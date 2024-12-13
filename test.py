n, p = map(int, input().split())

arr = []
value = n
while True:
    value = (value*n)%p
    if value in arr:
        break
    else:
        arr.append(value)

print(len(arr) - arr.index(value))