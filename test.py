arr = []
for _ in range(7):
    a, b = input().split()
    b = int(b)
    arr.append((a, b))

arr.sort(key=lambda x: -x[1])
print(arr[0][0])