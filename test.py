while True:
    m, a, b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        break

    train = m/a
    airplane = m/b

    time = (train-airplane)*3600
    time = round(time)

    h = time//3600
    time %= 3600
    m = time//60
    time %= 60
    s = time

    print(f'{h}:{m:02d}:{s:02d}')