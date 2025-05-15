n = int(input())

player = []
for i in range(1, n+1):
    s, c, l = map(int, input().split())
    player.append([s, c, l, i])

player.sort(key= lambda x:(-x[0], x[1], x[2]))

print(player[0][3])