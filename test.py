T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    h = max(arr[0]+arr[4], 1)
    m = max(arr[1]+arr[5], 1)
    a = max(arr[2]+arr[6], 0)
    b = arr[3]+arr[7]
    power = h+5*m+2*a+2*b
    print(power)