import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    mx = n
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        mx = max(mx, n)
    print(mx)