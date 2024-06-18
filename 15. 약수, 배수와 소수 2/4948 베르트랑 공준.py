import math
import sys

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    if x == 1:
        return False
    else:
        return True

data = 123456 * 2 # 문제에 주어진 모든 범위의 소수
primeArr = set()
for i in range(1, data+1):
    if isPrime(i) == True:
        primeArr.add(i)
    i += 1
# print(primeArr)

while True:
    a = int(input()) # 입력 값
    if a == 0: # 0일시 종료
        break
    ran = set(range(a+1, 2*a+1))
    print(len(ran & primeArr))