n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append(y)

print(max(arr)-min(arr))