while True:
    g, t, a, d = map(int, input().split())

    if g == -1 and a == -1 and t == -1 and d == -1:
        break
    
    x, y = 0, 0

    # 조별 리그
    group_match = t*(t-1)//2*g
    x += group_match

    # 토너먼트 진출 팀 수
    tournament = g*a+d

    value = 1
    while tournament > value:
        x += value
        value *= 2
    y += value-tournament
    
    print(f'{g}*{a}/{t}+{d}={x}+{y}')