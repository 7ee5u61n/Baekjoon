import math

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
          if x % i == 0:
               return False
    if x == 1:
         return False
    else:
        return True

M, N = map(int, input().split())

i = M
for i in range(M, N+1):
    if isPrime(i) == True:
        print(i)
    i += 1