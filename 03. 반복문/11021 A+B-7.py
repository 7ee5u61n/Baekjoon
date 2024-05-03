import sys
T = int(input()) #testCase
sumList = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    while A < 0 or A > 10 or B < 0 or B > 10:
        A, B = map(int,sys.stdin.readline().split())
        print('1~10 사이의 정수를 입력하시오')
    sumList.append(A + B)

for i in range(T):
    print('Case #'+str(i+1) +': ' + str(sumList[i]))
