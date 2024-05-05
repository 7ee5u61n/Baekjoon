import sys

N = int(input()) # 상점에 판매하는 무기의 수
X, S = map(int, input().split()) # 가진돈 X, 후안의 공격력 S
cList = []
pList = []

for _ in range(N):
    ci, pi = map(int, sys.stdin.readline().split()) # 무기의 가격 ci, 무기의 공격력 pi
    cList.append(ci) # 판매하는 무기의 가격 리스트
    pList.append(pi) # 판매하는 무기의 공격력 리스트

for i in range(N):
    if (cList[i] <= X and pList[i] > S): # 무기 가격과 소지금, 무기 공격력과 후안의 공격력을 비교
        print('YES')
        break # 조건을 만족하면 멈추고 출력
    else:
        print('NO')
        break