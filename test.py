import math

def isPrime(x): # x가 소수인지 확인하는 알고리즘
    for i in range(2, int(math.sqrt(x) + 1)):
          if x % i == 0:
               return False
    if x == 1:
         return True
    else:
        return True

S = str(input())
number = 0
for i in range(len(S)):
    if 65<=ord(S[i])<=96:
        number += ord(S[i])-38
    else:
         number += ord(S[i])-96

if isPrime(number):
    print('It is a prime word.')
else:
     print('It is not a prime word.')