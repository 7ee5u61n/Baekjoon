N = int(input())

generator = []

i = 0
for i in range(N):
    i += 1
    j = 0
    wholeSum = 0
    for j in range(len(str(i))):
        j += 1
        wholeSum += (i % ((10**j)//(10**(j-1)))) # 각 자리수의 합
    generator.append(wholeSum + i)
print(generator)