yeondu = str(input())
n = int(input())

team = []
for _ in range(n):
    team.append(str(input()))
team.sort()

most = 0
winner = team[0]
for i in range(n):
    L = yeondu.count('L') + team[i].count('L')
    O = yeondu.count('O') + team[i].count('O')
    V = yeondu.count('V') + team[i].count('V')
    E = yeondu.count('E') + team[i].count('E')
    win = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if win > most:
        most = win
        winner = team[i]

print(winner)