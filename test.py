import sys

N, P = map(int, sys.stdin.readline().split())

num = 1
for i in range(2, N+1):
    num = (num * i) % P

print(num % P)