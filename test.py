e, s, m = map(int, input().split())

E, S, M = 0, 0, 0
for i in range(15*28*19+1):
    E += 1
    if E > 15:
        E = 1
    S += 1
    if S > 28:
        S = 1
    M += 1
    if M > 19:
        M = 1
    if E == e and S == s and M == m:
        print(i + 1)
        break