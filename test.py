T = int(input())
for _ in range(T):
    n = int(input())
    w = 0
    for k in range(1, n+1):
        w += k*(sum(i for i in range(1, k+2)))
    print(w)