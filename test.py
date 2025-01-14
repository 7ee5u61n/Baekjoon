T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    if n * s > d + n * p:
        print('parallelize')
    elif n * s == d + n * p:
        print('does not matter')
    else:
        print('do not parallelize')
