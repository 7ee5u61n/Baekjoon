n = int(input())
arr = list(int(input()) for _ in range(n))

if arr[2]-arr[1] == arr[1] - arr[0]:
    print(arr[-1]+arr[1]-arr[0])
elif arr[2]//arr[1] == arr[1]//arr[0]:
    print(arr[-1]*(arr[1]//arr[0]))