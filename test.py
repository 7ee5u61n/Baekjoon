cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        break

    count = 0
    count += sum(cal[:month-1])
    # 윤년
    if (year % 4 == 0 and year % 100 != 0 and month > 2) or year % 400 == 0:
        count += 1
    count += day

    print(count)