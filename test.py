from collections import deque

n = int(input())
t = int(input())
hand = deque(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(len(b)):
    for j in range(b[i]-1):
        hand.append(hand.popleft())
    print(hand[0], end=' ')
    