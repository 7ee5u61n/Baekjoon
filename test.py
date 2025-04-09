n =int(input())
v = 0

A = list(map(float, input().split()))

for a in A:
    v = 1-((1-v)*(1-a/100))
    print(v*100)