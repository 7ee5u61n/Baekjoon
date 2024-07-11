A = int(input())
B = int(input())
C = int(input())

mul= str(A*B*C)

count = [0]*10

for i in range(10):
    for j in range(len(mul)):
        if int(mul[j]) == i:
            count[i] += 1

for i in range(len(count)):
    print(count[i])