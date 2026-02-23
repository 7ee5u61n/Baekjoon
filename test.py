import sys
input = sys.stdin.readline

def fact(n):
    value = 0
    lenth = len(str(n))
    for i in range(lenth):
        temp = 1
        for j in range(1, lenth-i+1):
             temp *= j
        temp *= int(str(n)[i])
        value += temp
    return value

while True:
    n = int(input())
    if n == 0:
        break
    print(fact(n))