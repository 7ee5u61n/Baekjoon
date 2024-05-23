import math
N = int(input())
while True:
    nList = list(input().rsplit())
    if len(nList) != N:
         print('다시 입력')
         continue
    else:
         break

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
          if x % i == 0:
               return False
    if x == 1:
         return False
    else:
        return True

count = 0
for i in range(N):
     if isPrime(int(nList[i])) == True:
          count += 1
print(count)