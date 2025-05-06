def dateToDay(date):
    day = 0
    for i in range(1, date[0]+1):
        if i in lunarYear:
            if i == date[0]:
                for j in range(1, date[1]+1):
                    if j == date[1]:
                        for k in range(1, date[2]+1):
                            day += 1
                    else:
                        for k in range(1, lunarMonth[j]+1):
                            day+= 1
            else:
                for j in range(1, 13):
                    for k in range(1, lunarMonth[j]+1):
                        day += 1

        else:
            if i == date[0]:
                for j in range(1, date[1]+1):
                    if j == date[1]:
                        for k in range(1, date[2]+1):
                            day += 1
                    else:
                        for k in range(1, month[j]+1):
                            day += 1
            else:
                for j in range(1, 13):
                    for k in range(1, month[j]+1):
                        day += 1
    return day

def thousand(date):
    day = 0
    for i in range(1, date[0]+1001):
        if i in lunarYear:
            if i == date[0]:
                for j in range(1, date[1]+1):
                    if j == date[1]:
                        for k in range(1, date[2]+1):
                            day += 1
                    else:
                        for k in range(1, lunarMonth[j]+1):
                            day+= 1
            else:
                for j in range(1, 13):
                    for k in range(1, lunarMonth[j]+1):
                        day += 1

        else:
            if i == date[0]:
                for j in range(1, date[1]+1):
                    if j == date[1]:
                        for k in range(1, date[2]+1):
                            day += 1
                    else:
                        for k in range(1, month[j]+1):
                            day += 1
            else:
                for j in range(1, 13):
                    for k in range(1, month[j]+1):
                        day += 1
    return day

lunarYear = set()
for i in range(1, 10000):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            continue
        else:
            lunarYear.add(i)

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
         7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
lunarMonth = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30,
         7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

today = list(map(int, input().split()))
dday = list(map(int, input().split()))

todayDay = dateToDay(today)
ddayDay = dateToDay(dday)
thousandDay = thousand(today)

if ddayDay >= thousandDay:
    print('gg')
else:
    print(f'D-{ddayDay - todayDay}')