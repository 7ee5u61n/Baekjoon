# 세로, 가로
n, m, x, y, k = map(int,input().split())
maps = [list(map(int, input().split())) for i in range(n)]

# 주사위 이동 명령
move = list(map(int, input().split()))
# 주사위 위치
locate = [x, y]
# 주사위 숫자
dice = [[0, 0] for i in range(3)]
temp = [[0, 1], [2, 3]]

# 주사위 회전 정의
def roll(d):
    # 동
    if d == 1:
        dice[2].reverse()
        dice[2], dice[0] = dice[0], dice[2]
    # 서
    elif d == 2:
        dice[0].reverse()
        dice[0], dice[2] = dice[2], dice[0]
    # 북
    elif d == 3:
        dice[1].reverse()
        dice[1], dice[0] = dice[0], dice[1]
    # 남
    else:
        dice[0].reverse()
        dice[0], dice[1] = dice[1], dice[0]

# 이동 방향
d = 1
# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(k):
    # print(maps, i)
    # print(locate, i)
    # print(dice)
    d = move[i]
    nx = locate[0] + dx[d-1]
    ny = locate[1] + dy[d-1]

    if 0<=nx<n and 0<=ny<m:
        # 주사위 회전
        roll(d)
        # 바닥면이 0이라면
        if maps[nx][ny] == 0:
            # 주사위 바닥면 복사
            maps[nx][ny] = dice[0][1]
        else:
            dice[0][1] = maps[nx][ny] # 칸에 쓰인 숫자 주사위에 복사
            maps[nx][ny] = 0
        locate[0] = nx
        locate[1] = ny
        print(dice[0][0])