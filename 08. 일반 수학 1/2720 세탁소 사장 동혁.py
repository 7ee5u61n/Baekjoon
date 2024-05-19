# 쿼터 25 다임 10 니켈 5 페니 1
T = int(input()) # 테스트 케이스 개수
cList = [] # 거스름돈 리스트

for i in range(T):
    C = int(input()) # 거스름돈 센트
    cList.append(C)

for i in range(len(cList)):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    while True:
        result = []
        quarter = cList[i] // 25
        remain = cList[i] % 25
        dime = remain // 10
        remain = remain % 10
        nickel = remain // 5
        remain = remain % 5
        penny = remain // 1
        result.append(quarter)
        result.append(dime)
        result.append(nickel)
        result.append(penny)
        print(*result)
        break