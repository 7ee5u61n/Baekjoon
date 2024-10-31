d = [0]*12
for i in range(1, 12):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 2
    elif i == 3:
        d[i] = 4
    else:
        d[i] = d[i-1]+d[i-2]+d[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])