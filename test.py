import sys
input = sys.stdin.readline

r, k, m = map(int, input().split())

for _ in range(m//k):
    r //= 2
    if r < 1:
        break
    
print(r)