s = int(input())
ma, f, mb = map(int, input().split())

if s <= 240:
    print('high speed rail')
else:
    flight_time = ma + f + mb
    if flight_time >= s:
        print('high speed rail')
    else:
        print('flight')
