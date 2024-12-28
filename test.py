T = int(input())
for _ in range(T):
    n, m, k, d = map(int, input().split())

    b = 2*d//(n*m*(m-1)*k + n*(n-1)*m*m)

    if b:
        game = n*m*(m-1)*k*b//2 + n*(n-1)*m*m*b//2
        print(game)
    else:
        print(-1)