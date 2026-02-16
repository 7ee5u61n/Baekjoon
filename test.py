import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a = int(input())
    b = int(bin(a)[2:])
    
    if b&(~b+1) == a:
        print(1)
    else:
        print(0)