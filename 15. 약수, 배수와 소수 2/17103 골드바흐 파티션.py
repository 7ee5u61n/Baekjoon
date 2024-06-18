import sys

primeArr = [True for _ in range(1000001)] # 주어진 범위 내의 소수
# 0, 1 예외 처리
primeArr [0] = False 
primeArr [1] = False

for i in range(2, 1000001):
    if primeArr[i]:
        for j in range(i*2, 1000001, i):
            primeArr[j] = False

T = int(input()) # 테스트 케이스 개수

for i in range(T):
    N = int(sys.stdin.readline())
    partitions = 0 # 골드버그 파티션의 수
    for j in range(2, N//2+1):
        if primeArr[j] and primeArr[N-j]:
            partitions += 1
    print(partitions)