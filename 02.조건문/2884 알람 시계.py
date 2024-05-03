import datetime as dt

H, M = map(int, input().split())

changyongTime = (M - 45)

if H == 0 and changyongTime < 0:
    print(23, 60 + changyongTime)

elif changyongTime < 0:
    print(H-1, (60 + changyongTime))
else:
    print(H, changyongTime)