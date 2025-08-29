year = 2024
month = 8

n = int(input())


month += 7*(n-1)

if month > 12:
    year += month // 12
    month = month % 12
    if month == 0:
        month = 12
        year -= 1

print(year, month)