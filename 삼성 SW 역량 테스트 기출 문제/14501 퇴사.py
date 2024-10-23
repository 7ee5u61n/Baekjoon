n = int(input())

schedule = []
for i in range(n):
    # 상담 기간, 금액
    t, p = map(int, input().split())
    schedule.append([t,p])

d = [0]*(n+1)
for i in range(n-1, -1, -1):
    day = schedule[i][0]
    price = schedule[i][1]
    if i+schedule[i][0] <= n:
        d[i] = max(d[i+1], d[i+day]+price)
    else:
        d[i] = d[i+1]

print(d[0])