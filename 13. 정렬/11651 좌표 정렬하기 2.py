N = int(input())

coordinate = []
for i in range(N):
    xy = list(map(int, input().split()))
    coordinate.append(xy)
coordinate.sort(key= lambda x:(x[1],x[0]))

for i in range(len(coordinate)):
    print(*coordinate[i])