import sys

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

mina = 0
minb = 0
minrss = sys.maxsize
for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for x, y in arr:
            rss += (y-(a*x+b))**2
        
        if minrss > rss:
            minrss = rss
            mina = a
            minb = b

print(mina, minb)