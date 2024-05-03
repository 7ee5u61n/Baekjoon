testCase = int(input())
sumList = []

for i in range(testCase):
    A, B = map(int, input().split())
    while A < 1 or B < 1 or A > 9 or B > 9:
        print('1~10 사이의 값을 입력')
        A, B = map(int, input().split())
    sumList.append(A+B)

for i in range(testCase):
    print(sumList[i])