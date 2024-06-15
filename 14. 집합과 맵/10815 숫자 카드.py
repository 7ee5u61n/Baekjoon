import sys
N = int(input())
sanguenCard = set(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는 카드
M = int(input())
cards = list(map(int, sys.stdin.readline().split())) # 비교할 카드

for i in range(M):
    if cards[i] in sanguenCard:
        sys.stdout.write(str(1) + ' ')
    else:
        sys.stdout.write(str(0) + ' ')
