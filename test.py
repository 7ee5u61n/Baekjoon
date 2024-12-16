T = int(input())
for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    # 겹치는 부분 좌표
    dx = []
    dy = []
    for i in range(x3, x4+1):
        if x1 <= i <= x2:
            dx.append(i)
    for i in range(y3, y4+1):
        if y1 <= i <= y2:
            dy.append(i)

    # 포스터 넓이
    poster1 = (x2-x1)*(y2-y1)
    # 겹치는 부분 넓이
    poster2 = 0
    if dx and dy:
        poster2 = (dx[-1]-dx[0])*(dy[-1]-dy[0])

    result = poster1 - poster2
    print(result)