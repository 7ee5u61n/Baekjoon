N, X, K = map(int, input().split())
where = X

for _ in range(K):
    a, b = map(int, input().split())
    if a == where:
        where = b
    elif b == where:
        where = a

print(where)