import sys
import math

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
          if x % i == 0:
               return False
    if x == 1:
         return False
    else:
        return True

n = int(input()) # 테스트 케이스 개수

numers = []
for _ in range(n):
    a = int(sys.stdin.readline())
    i = 0
    while True:
        if a == 0 or a == 1: # 0과 1 예외 처리
             print(2)
             break
        elif isPrime(a+i) == True:
            print(a+i)
            break
        i += 1