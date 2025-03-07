n = int(input())
a = list(map(int, input().split()))

arithmetical = True
if n > 2:
    degree = a[1] - a[0]
    for i in range(1, n-1):
        if a[i+1] - a[i] != degree:
            arithmetical = False
            break

if arithmetical:
    b = a
    c = [0]*n
    print('YES')
    print(*b)
    print(*c)
else:
    print('NO')