yt, yj = map(int, input().split())

# 1 == 용태 공격, 0 == 유진 공격
turn = 1
while yt < 5 or yj < 5:
    if turn:
        yj += yt
        turn = 0
    else:
        yt += yj
        turn = 1

if yt > yj:
    print("yt")
else:
    print("yj")