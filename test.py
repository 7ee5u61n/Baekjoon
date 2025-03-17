n = int(input())
x = list(map(int, input().split()))
x = sorted(x)

team = 0
limit = x[0]
member = 0
for i in range(n):
    if member == 0:
        limit = x[i]
    member += 1

    if member == limit:
        team += 1
        member = 0

if member:
    team += 1

print(team)