import math
M = int(input())
N = int(input())

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
          if x % i == 0:
               return False
    if x == 1:
         return False
    else:
        return True

primeNumber = []
i = M
while i <= N:
    if isPrime(i) == True:
        primeNumber.append(i)
    i += 1

if bool(primeNumber) == True:
    print(sum(primeNumber))
    print(primeNumber[0])
else:
    print(-1)