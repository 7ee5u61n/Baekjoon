T = int(input())
for _ in range(T):
    n = int(input())
    pig = list(map(int, input().split()))
    
    yesterday = [0]*6
    for i in range(6):
        yesterday[i] = pig[i]

    day = 1
    while True:
        # 먹이 못 줘
        if sum(pig) > n:
            break
        
        for i in range(6):
            # 전 날 , 왼쪽, 오른쪽, 맞은편
            pig[i] = yesterday[i] + yesterday[(i-1)%6]+yesterday[(i+1)%6]+yesterday[(i+3)%6]
        
        for i in range(6):
            yesterday[i] = pig[i]
        
        day += 1

    print(day)