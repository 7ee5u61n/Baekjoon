from collections import deque

# 왼쪽 확인
def left(idx, dist):
    if idx > 0:
        if gear[idx][6] != gear[idx-1][2]:
            left(idx-1, -dist)
            gear[idx-1].rotate(dist)
    # 벗어나면 종료
    else:
        return

# 오른쪽 확인
def right(idx, dist):
    if idx < 3:
        if gear[idx][2] != gear[idx+1][6]:
            right(idx+1, -dist)
            gear[idx+1].rotate(dist)
    else:
        return

gear = [deque(list(map(int, input()))) for _ in range(4)]

k = int(input())
for _ in range(k):
    # 톱니 번호, 방향
    idx, dist = map(int, input().split())
    # 번호와 인덱스 같게 하기
    idx -= 1
    # 왼쪽, 오른쪽 확인
    left(idx, -dist)
    right(idx, -dist)
    # 첫 톱니바퀴 회전
    gear[idx].rotate(dist)

# 점수 계산
score = 0
point = 1
for i in range(4):
    # S극이면 점수
    if gear[i][0] == 1:
        score += point
    point *= 2

print(score)