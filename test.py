while True:
    try:
        m, p, l, e, r, s, n = map(int, input().split())
    except:
        break
    for i in range(n):
        mp = m
        m = p//s
        p = l//r
        l = mp*e

    print(m)