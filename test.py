N, M = map(int, input().split())
castle = []

for _ in range(N):
    castle.append(list(input()))        

emptyCol = 0
emptyRow = 0

for i in castle:
    if "X" not in i:
        emptyCol += 1

for i in range(M):
    if "X" not in [castle[j][i] for j in range(N)]:
        emptyRow += 1

print(max(emptyCol, emptyRow))