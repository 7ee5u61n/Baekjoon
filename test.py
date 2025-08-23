import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    a = n//m
    b = n % m
    c = m

    print(f'{a} {b} / {c}')