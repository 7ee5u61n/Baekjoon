a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())

fx = a1 * n0 + a0
gx = n0

if c1*gx <= fx <= c2*gx:
    print(1)
else:
    print(0)