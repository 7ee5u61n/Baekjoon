n, m = map(int, input().split())
a, d = map(int, input().split())
x, y = map(int, input().split())

if x == n and n % 2 != d:
    print('YES!')
else:
    print('NO...')