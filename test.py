import sys

N, M = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
sum = [0]
temp = 0

for i in number:
    temp += i
    sum.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum[j] - sum[i-1])