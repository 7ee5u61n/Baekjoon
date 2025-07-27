
n, m = map(int, input().split())

bessie = []
# 총 시간
totalTime = 0
for _ in range(n):
    speed, time = map(int, input().split())
    totalTime += time
    bessie.append((speed, time))

elsie = []
for _ in range(m):
    speed, time = map(int, input().split())
    elsie.append((speed, time))

# 각자 위치
bessiePosition = 0
elsiePosition = 0

# 현재 선두
currentLeader = -1

# 현재 속도 인덱스
bessieIndex = 0
elsieIndex = 0

# 달린 유닛 시간
bessieUnitTime = 0
elsieUnitTime = 0

# 선두 변경 횟수
count = 0
for _ in range(totalTime):
    bessiePosition += bessie[bessieIndex][0]
    elsiePosition += elsie[elsieIndex][0]

    # 각자 유닛 시간 증가
    bessieUnitTime += 1
    elsieUnitTime += 1

    # 현재 속도 인덱스가 가리키는 시간만큼 달렸다면 인덱스 증가
    if bessieUnitTime == bessie[bessieIndex][1]:
        bessieIndex += 1
        bessieUnitTime = 0

    if elsieUnitTime == elsie[elsieIndex][1]:
        elsieIndex += 1
        elsieUnitTime = 0

    # 선두 확인
    if bessiePosition > elsiePosition:
        # 베시
        leadership = 1
    elif elsiePosition > bessiePosition:
        # 엘시
        leadership = 0 
    else:
        # 동점
        leadership = 2

    # 선두 변경
    if currentLeader == -1:
        currentLeader = leadership
    elif leadership != 2 and leadership != currentLeader:
        if currentLeader == 2:
            currentLeader = leadership
        elif currentLeader != 2 and leadership != currentLeader:
            count += 1
            currentLeader = leadership

print(count)