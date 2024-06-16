import sys

T = int(input())

def GCD(x, y): # 최대공약수
    while(y):
        x, y = y, x % y
    return x

def LCM(x, y): # 최소공배수
    result = (x * y) // GCD(x, y)
    return result

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(LCM(A, B))