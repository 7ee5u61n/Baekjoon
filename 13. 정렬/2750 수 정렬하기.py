N = int(input())
nList = []
for i in range(N):
    nList.append(int(input()))
nList = sorted(nList)
for i in range(len(nList)):
    print(nList[i])