n = int(input())

condo = [list(map(int, input().split())) for _ in range(n)]
condo.sort()

price = condo[0][1]
result = 1
for i in range(1, n):
    if condo[i][1] < price:
        result += 1
        price = condo[i][1]

print(result)