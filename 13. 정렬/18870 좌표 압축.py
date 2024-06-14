N = int(input())
X = list(map(int, input().split()))

sortedX = sorted(set(X))

dictX = {}
for i in range(len(sortedX)):
    dictX[sortedX[i]] = i

for i in X:
    print(dictX[i], end=" ")