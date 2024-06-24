from collections import deque

N = int(input())

cards = deque(range(1, N+1))

for i in range(N-1):
    cards.popleft() # 제일 위에 카드 버리기
    cards.append(cards.popleft()) # 제일 위에 있는 카드 제일 아래로

print(*cards)