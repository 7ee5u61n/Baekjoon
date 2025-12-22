T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    result = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v * (f/c) >= d:
            result += 1
    print(result)