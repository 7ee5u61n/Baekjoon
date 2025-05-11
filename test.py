n, x = map(int, input().split())
a = list(map(int, input().split()))

socks = 2000
for i in range(n-1):
    socks = min(a[i]+a[i+1], socks)

print(socks*x)