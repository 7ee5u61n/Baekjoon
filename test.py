n, k = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    temp = ''
    for j in range(n):
        temp += ((str(arr[i][j])+' ')*k)
    for j in range(k):
        print(temp)