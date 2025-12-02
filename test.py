k, n = map(int, input().split())

# (x - k) * n >= x
# x >= (k * n) / (n - 1)

if n == 1:
    print(-1)
else:
    x = (k * n) // (n - 1)
    if ((k * n) % (n - 1)):
        x += 1
    print(x)