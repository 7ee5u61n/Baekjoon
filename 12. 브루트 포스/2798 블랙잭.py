from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))

C = list(combinations(card, 3)) # 3장 뽑아 나올 수 있는 경우의 수

sumList = []
for i in range(len(C)): # 카드 3장의 모든 합
    sumList.append(sum(list(C[i])))

sumList = sorted(sumList)
for i in range(len(sumList)): # M보다 크지 않으면서 가장 큰 값
    if sumList[i] <= M:
        maxValue = sumList[i]

print(maxValue)