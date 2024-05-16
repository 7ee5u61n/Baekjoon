N, M = map(int, input().split()) # N * M 크기의 행렬row = []
array = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    row = input().split()
    for j in range(M):
        array[i][j] += int(row[j])
for i in range(N):
    row = input().split()
    for j in range(M):
        array[i][j] += int(row[j])
for i in range(N):
    for j in range(M):
        print(array[i][j], end = ' ')
    print()