a, b = map(int, input().split())

arr = []
for i in range(b+1):
    arr += [i]*i

print(sum(arr[a-1:b]))