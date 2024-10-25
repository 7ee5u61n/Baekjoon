from collections import deque

# 보드의 크기
n = int(input())
# 사과의 개수
k = int(input())
apples = []
for i in range(k):
    row, column = map(int, input().split())
    apples.append([column, row])

# 방향 전환 횟수
l = int(input())
turn = []
for i in range(l):
    x, c = input().split()
    turn.append([x, c])
head = [1, 1]
tail = deque()

# 동, 남, 서, 북
d = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
time = 0
while True:
    time += 1
    nx = head[0]+dx[d]
    ny = head[1]+dy[d]
    # 다음 이동할 칸
    next_head = [nx, ny]

    # print(apples)
    # print(next_head, time)
    # print(head, time)
    # print(tail, time)
    
    # 꼬리에 충돌하는 경우
    if next_head in tail:
        break
    if 1<=next_head[0]<=n and 1<=next_head[1]<=n:
        # 사과를 먹은 경우
        if next_head in apples:
            apples.remove(next_head) # 사과가 맵에서 사라짐
            tail.appendleft(head)
            head = next_head
        else:
            tail.appendleft(head)
            tail.pop()
            head = next_head
    # 벽을 만남
    else:
        break
    # 방향 전환 시간
    if turn:
        if time == int(turn[0][0]):
            if turn[0][1] == 'L':
                d = (d-1)%4 # 왼쪽
            else:
                d = (d+1)%4 # 오른쪽
            turn.pop(0)

print(time)