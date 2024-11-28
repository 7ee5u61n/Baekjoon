def calcArea(a, b, c, d):
    return ((c-a)+(d-b))*2

n = int(input())
a, b, c, d = map(int, input().split())
print(calcArea(a, b, c, d))

for _ in range(n-1):
    newA, newB, newC, newD = map(int, input().split())
    a = min(a, newA)
    b = min(b, newB)
    c = max(c, newC)
    d = max(d, newD)
    print(calcArea(a,b,c,d))