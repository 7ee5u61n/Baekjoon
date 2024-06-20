import sys

N = int(sys.stdin.readline()) # 명령의 수

stack = []

for i in range(N):
    order = str(sys.stdin.readline().rstrip()) # 주어진 명령
    if order[0] == str(1):
        stack.append(order[2:])
    
    elif order[0] == str(2):
        if stack:
            print(stack.pop(-1))
            continue
        print(-1)
        
    elif order[0] == str(3):
        print(len(stack))
    
    elif order[0] == str(4):
        if bool(stack) == False:
            print(1)
        else:
            print(0)
    
    elif order[0] == str(5):
        if stack:
            print(stack[-1])
        else:
            print(-1)