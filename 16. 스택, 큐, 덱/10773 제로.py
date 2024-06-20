import sys

K = int(input())

stack = []

for _ in range(K):
    number = int(sys.stdin.readline().rstrip())

    if number != 0:
        stack.append(number)
    else:
        stack.pop(-1)
    
print(sum(stack))