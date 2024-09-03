N = int(input())
Adrian = []
for i in range(N):
    if i % 3 == 0:
        Adrian.append('A')
    elif i % 3 == 1:
        Adrian.append('B')
    else:
        Adrian.append('C')

Bruno = []
for i in range(N):
    if i % 4 == 0 or i % 4 == 2:
        Bruno.append('B')
    elif i % 4 == 1:
        Bruno.append('A')
    else:
        Bruno.append('C')

Goran = []
for i in range(N):
    if i % 6 == 0 or i % 6 == 1:
        Goran.append('C')
    elif i % 6 == 2 or i % 6 == 3:
        Goran.append('A')
    else:
        Goran.append('B')

solution = str(input())

pointA = 0
pointB = 0
pointG = 0
for i in range(N):
    if solution[i] == Adrian[i]:
        pointA += 1
    
    if solution[i] == Bruno[i]:
        pointB += 1

    if solution[i] == Goran[i]:
        pointG += 1

winner = max(pointA, pointB, pointG)
print(winner)
if winner == pointA:
    print('Adrian')
if winner == pointB:
    print('Bruno')
if winner == pointG:
    print('Goran')