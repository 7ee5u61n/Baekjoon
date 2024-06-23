import sys
from collections import deque

N = int(input())

queue = deque([])

for i in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push': # 정수 X를 큐에 넣는 연산
        X = order[1]
        queue.append(X)
    
    elif order[0] == 'pop': # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    
    elif order[0] == 'size': # 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    
    elif order[0] == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if queue:
            print(0)
        else:
            print(1)
    
    elif order[0] == 'front': # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order[0] == 'back': # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[-1])
        else:
            print(-1)