import sys
from collections import Counter

N = int(input())
sanguenCard = list(map(int, sys.stdin.readline().split()))

countCard = dict(Counter(sanguenCard))

M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    try:
        print(countCard[cards[i]], end=" ")
    except:
        print(0, end=" ")