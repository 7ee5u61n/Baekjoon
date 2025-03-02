import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

lenth = 0
for i in range(n):
    for j in range(n):
        lenth += abs(x[i]-x[j])

print(lenth)