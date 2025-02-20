n, m = map(int, input().split())
cost = [int(input()) for _ in range(n)]

point = [0]*n
for i in range(m):
    judge = int(input())
    for j in range(n):
        if cost[j] <= judge:
            point[j] += 1
            break

print(point.index(max(point))+1)