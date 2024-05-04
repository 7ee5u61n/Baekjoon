A = int()
B = int()

sumList = [] # A + B

while True:
    try:
        A, B = map(int, input().split())
        sumList.append(A + B)
    except:
        break
T = len(sumList)

for i in range(T):
    print(sumList[i])