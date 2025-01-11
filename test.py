n = int(input())
for _ in range(n):
    m = int(input())
    mission = []
    for _ in range(m):
        mission.append(list(map(int, input().split())))
    k, d, a = map(int, input().split())

    donation = 0
    for K, D, A in mission:
        if (K*k)-(D*d)+(A*a) >= 0:
            donation += (K*k)-(D*d)+(A*a)
        
    print(donation)