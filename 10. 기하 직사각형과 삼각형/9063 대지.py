import sys
N = int(input())
xList = []
yList = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xList.append(x)
    yList.append(y)

lenth = max(xList) - min(xList) # 길이
height = max(yList) - min(yList) # 높이
area = lenth*height # 넓이

print(area)