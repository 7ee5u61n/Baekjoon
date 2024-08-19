import sys

A = int(sys.stdin.readline())
operator = str(input())
B = int(sys.stdin.readline())

if operator == '+':
    print(A + B)
else:
    print(A * B)