from collections import deque

# 보드의 크기
n = int(input())
# 사과의 개수
k = int(input())

# 사과의 위치
apples = []
for i in range(k):
    row, column = map(int, input().split())
    apples.append([column, row])

head = [1, 1]
tail = deque()

# 움직이는 방향 (동, 남, 서, 북)
di = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 방향 변환 횟수
l = int(input())
move = deque()
for i in range(l):
    move.append(input().split())

time = 0
while True:
    # 시간
    time += 1

    # 다음 머리 위치
    next_head = [head[0]+dx[di], head[1]+dy[di]]
    # print(apples)
    # print(f'방향: {di}')
    # print(f'next_head: {next_head, time}')
    # print(f'head:{head, time}')
    # print(f'tail:{tail, time}')
    tail.appendleft(head)
    if next_head not in tail:
        # 맵 안
        if 1 <= next_head[0] <= n and 1 <= next_head[1] <= n:
            # 사과 먹음
            if next_head in apples:
                # print('eat', time)
                apples.remove(next_head)
                head = next_head
            else:
                if tail:
                    tail.pop()
                head = next_head
        # 맵 벗어남
        else:
            # print('맵 벗어남')
            break
    # 꼬리에 닿음
    else:
        # print('꼬리 충돌')
        break
        
    # 방향 전환 시간
    if move:
        if time == int(move[0][0]):
            # 왼쪽
            if move[0][1] == 'L':
                di = (di-1)%4
            else:
                di = (di+1)%4
            move.popleft()

print(time)