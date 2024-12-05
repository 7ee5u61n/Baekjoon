n, m = input().split()

player = set()
for _ in range(int(n)):
    player.add(str(input()))

if m == 'Y':
    print(len(player))
elif m == 'F':
    print(len(player)//2)
else:
    print(len(player)//3)