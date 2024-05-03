import sys
testCase = int(input())
sumList = []

for i in range(testCase):
    A,B = map(int, sys.stdin.readline().split())
    sumList.append(A + B)

for i in range(testCase):
    print(sumList[i])