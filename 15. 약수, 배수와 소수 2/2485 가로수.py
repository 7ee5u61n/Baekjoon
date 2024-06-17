import sys
import math

def GCD(x, y): # 최대공약수
    while(y):
        x, y = y, x % y
    return x

def GCD_N(arr): # 리스트에 있는 모든 값들의 최대공약수
    gcd = arr[0]
    for item in arr:
        gcd = GCD(gcd, item)
    return gcd

N = int(input()) # 심어져 있는 가로수의 수

trees = [] # 심어져 있는 가로수 위치
for i in range(N):
    trees.append(int(sys.stdin.readline().rstrip()))

distance = [] # 심어져 있는 가로수 사이의 간격
for i in range(N-1):
    distance.append(abs(trees[i+1] - trees[i]))

gap = GCD_N(distance) # 심을 간격

planting = 0 # 심을 갯수

for i in distance:
    planting += i // gap - 1

print(planting)