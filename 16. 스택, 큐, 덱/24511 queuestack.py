import sys
from collections import deque

N = int(input())

order1 = list(map(int, sys.stdin.readline().split())) # 큐(0) 인지 스택(1) 인지
order2 = list(map(int, sys.stdin.readline().split())) # i번 자료구조에 들어 있는 원소
order3 = int(input()) # 삽입할 원소의 수
order4 = list(map(int, sys.stdin.readline().split())) # 삽입할 원소

result = deque()

for i in range(N):
    if order1[i] == 0:
        result.append(order2[i])

for j in range(order3):
    result.appendleft(order4[j])

for k in range(order3):
    print(result.pop(), end= ' ')