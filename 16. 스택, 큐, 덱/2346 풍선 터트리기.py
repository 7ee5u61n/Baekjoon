from collections import deque

N = int(input())

order = deque(map(int, input().split())) # 풍선에 적힌 숫자
balloons = deque(range(1, N+1)) # N번 까지 풍선 번호
sequence = [] # 풍선 터트리는 순서

while True:
    thisPop = order.popleft() # 이번에 터트리는 번호
    sequence.append(balloons.popleft())
    if len(order) == 0:
        break
    
    if thisPop > 0:
        for _ in range(thisPop-1):
            order.append(order.popleft())
            balloons.append(balloons.popleft())
    else:
        for _ in range(abs(thisPop)):
            order.appendleft(order.pop())
            balloons.appendleft(balloons.pop())

print(*sequence)