chuck = list(map(int, input().split()))
eungyu = list(map(int, input().split()))

cho = 0
han = 1.5

point = [13, 7, 5, 3, 3, 2]

for i in range(6):
    cho += chuck[i] * point[i]
    han += eungyu[i] * point[i]

if cho > han:
    print('cocjr0208')
else:
    print('ekwoo')