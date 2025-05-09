n, k, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    i = int(input())
    if i > 0:
        if i >= k:
            k = i-k+1
    else:
        if i < k-n:
            k = i+n-(k-n-1)

print(k)