n, m, k = map(int, input().split())

o = max(0, m-k)
x = max(0, (n-m)-(n-k))
print(n - (o + x))