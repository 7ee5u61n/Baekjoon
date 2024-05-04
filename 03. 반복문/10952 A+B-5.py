A = int()
B = int()

sumList = [] # A + B

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    sumList.append(A + B)

T = len(sumList)

for i in range(T):
    print(sumList[i])