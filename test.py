T = int(input())

for _ in range(T):
    N = int(input())

    whale = ''
    amount = 0

    for _ in range(N):
        S, L = input().split()
        L = int(L)

        if L > amount:
            amount = L
            whale = S

    print(whale)