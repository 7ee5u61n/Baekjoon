import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    # push
    if len(order) == 2:
        stack.append(int(order[1]))
    else:
        # pop
        if order[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        # size
        elif order[0] == 'size':
            print(len(stack))
        # empty
        elif order[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        # top
        elif order[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)