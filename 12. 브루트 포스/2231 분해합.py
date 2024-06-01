N = int(input())

generator = []
for i in range(1, N+1):
    j = 1
    wholeSum = 0
    for j in range(len(str(i))):
        j += 1
        wholeSum += (i % (10**j)//(10**(j-1))) # 각 자리수의 합
    if wholeSum + i == N: # 가장 작은 생성자
        print(i)
        break
    if i == N:
        print(0)