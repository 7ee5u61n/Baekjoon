year, month, day = map(int, input().split())
y, m, d = map(int, input().split())

manAge = 0
seneunAge = 0
yeonAge = 0

manAge = y-year
if month > m or (month == m and day > d):
    manAge -= 1

seneunAge = y-year+1

if year == y:
    yeonAge = 0
else:
    yeonAge = y-year

print(manAge)
print(seneunAge)
print(yeonAge)