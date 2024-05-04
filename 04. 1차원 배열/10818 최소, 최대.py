import sys

N = int(input()) # 정수의 개수 N
A = list(map(int, sys.stdin.readline().split())) # 수열 A

minInt = min(A)
maxInt = max(A)

print(minInt, maxInt)